from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app.domain import Client, Metric, months, recoveryPhrase
from app.marsh import clientSchema
from app.ext import db, getValidMonth
from uuid import uuid4
from app.tasks import sendEmail
from requests import get
from time import time
from decimal import Decimal
import re
from datetime import datetime



app = Blueprint('ClientPage', __name__)
debtPattern = re.compile("^[0-9]{1,9}\.[0-9]{2}$")



@app.route("/")
@login_required
def defaultPrivatePage():
  client = Client.query.get(current_user.id)
  return render_template("defaultPrivatePage.tpl", client = clientSchema.dump(client).data)



@app.route("/edit/")
@login_required
def showEditDialog():
  client = Client.query.get(current_user.id)
  return render_template("showEditDialog.tpl", client = clientSchema.dump(client).data)



@app.route("/edit/", methods = ["post"])
@login_required
def editData():
  client = Client.query.get(current_user.id)
  client.setTelephone(request.form.get("telephone", ""))
  client.setEmail(request.form.get("email", ""))
  db.session.commit()
  return redirect(url_for('ClientPage.defaultPrivatePage'))


@app.route("/enter/")
def showLoginForm():
  return render_template("enter.tpl")



@app.route("/enter/", methods = ["post"])
def loginUser():
  login = request.form.get("login", "").strip().replace("-", "")
  password = request.form.get("password", "").strip()
  user = Client.query.filter_by(number = login).one_or_none()
  if user and user.password == Client.generateHash(password):
    user.is_active = True
    user.is_authenticated = True
    login_user(user)
  return redirect(url_for('ClientPage.defaultPrivatePage'))



@app.route("/logout/")
@login_required
def logout():
  logout_user()
  return redirect(url_for('ClientPage.showLoginForm'))



@app.route("/metrics/")
@login_required
def showMetricsPage():
  lastMetrics = {}
  currentMetrics = {}
  now = getValidMonth()
  month = now.strftime("%Y%m")
  client = Client.query.get(current_user.id)
  mday = datetime.now().day
  if mday > 25 or mday < 23:
    return render_template("showNoMetricsPage.tpl", client = client)

  for pu in client.pus:
    #last
    metrics = Metric.query.filter(Metric.month != month).filter_by(pu = pu).order_by(Metric.month.desc()).limit(1).all()
    for metric in metrics:
      lastMetrics[metric.pu.id] = metric.m.split(";")
    # current
    metrics = Metric.query.filter_by(pu = pu, month = month).order_by(Metric.month.desc()).limit(1).all()
    for metric in metrics:
      currentMetrics[metric.pu.id] = metric.m.split(";")
  client = clientSchema.dump(client).data
  return render_template("showMetricsPage.tpl", client = client, lastMetrics = lastMetrics, currentMetrics = currentMetrics, month = month, months = months)



@app.route("/metrics/", methods = ["post"])
@login_required
def updateMetrics():
  now = getValidMonth()
  month = now.strftime("%Y%m")
  client = Client.query.get(current_user.id)
  for pu in client.pus:
    name1 = "{}:m1".format(pu.id)
    name2 = "{}:m2".format(pu.id)
    m1parts = request.form.get(name1, "0.00").replace("_", "").split(".")
    m2parts = request.form.get(name2, "0.00").replace("_", "").split(".")
    if m1parts[1] == "" or len(m1parts[1]) == 1:
      m1parts[1] = "00"
    if m2parts[1] == "" or len(m2parts[1]):
      m2parts[1] = "00"
    m1 = ".".join(m1parts)
    m2 = ".".join(m2parts)
    metric = Metric.query.filter_by(pu = pu, month = month).one_or_none()
    if metric:
      metric.setM(m1, m2)
    else:
      metric = Metric(pu, now, m1, m2)
      db.session.add(metric)
  db.session.commit()
  return render_template("successMetricsPage.tpl")



@app.route("/recovery/")
def showRecoveryForm():
  return render_template("recovery/showRecoveryForm.tpl")



@app.route("/recovery/", methods = ["post"])
def recoveryPassword():
  login = request.form.get("login", "").strip().replace("-", "")
  client = Client.query.filter_by(number = login).one_or_none()
  if client:
    if len(client.email) > 0:
      password = uuid4().hex[:6]
      client.setPasswordHash(Client.generateHash(password))
      db.session.commit()
      sendEmail.delay(client.email, "Восcтановление пароля от личного кабинета", recoveryPhrase.format(client.number[:-2], client.number[-2:], password, current_app.config["SITE_URL"]))
      return render_template("recovery/successRecoveryPassword.tpl")
    else:
      return render_template("recovery/notFoundEmailRecoveryPassword.tpl")
  else:
    return render_template("recovery/notFoundClientRecoveryPassword.tpl")



@app.route("/pay/")
@login_required
def showPayPage():
  debt = Decimal(current_user.debt)
  penalty = Decimal(current_user.penalty)
  return render_template("pay/payPage.tpl", debt = debt, penalty = penalty)



@app.route("/pay/", methods = ["post"])
@login_required
def processPayPage():
  if "penaltySubmit" in request.form:
    debt = request.form.get("penalty", "0.00")
  else:
    debt = request.form.get("debt", "0.00")
  if not debtPattern.match(debt):
    return render_template("pay/payPageFailrure.tpl")
  params = {
    "userName": current_app.config["SBER_LOGIN"],
    "password": current_app.config["SBER_PASSWORD"],
    "orderNumber": "{}-{}".format(current_user.number, int(time())),
    "amount": debt.replace(".", ""),
    "returnUrl": current_app.config["SBER_RETURN_URL"]
  }
  r = get("https://securepayments.sberbank.ru/payment/rest/register.do", params = params)
  if r.status_code == 200:
    json = r.json()
    if "formUrl" in json:
      return redirect(json["formUrl"])
  return render_template("pay/payPageFailrure.tpl")



@app.route("/pay/success/")
@login_required
def showSuccessPayPage():
  return render_template("pay/showSuccessPayPage.tpl")