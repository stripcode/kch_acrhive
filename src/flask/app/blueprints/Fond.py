from flask import Blueprint, render_template, request, redirect, current_app
from app.domain import Client, Metric, recoveryPhrase
from app.ext import db
from app.tasks import sendEmail
from sqlalchemy import distinct
from uuid import uuid4
from app.marsh import clientSchema, clientsSchema, metricsSchema
from datetime import datetime



app = Blueprint('Fond', __name__)



@app.route("/")
def showFondPage():
  cities = db.session.query(distinct(Client.cityName)).order_by(Client.cityName.asc()).all()
  return render_template("fond/showFondPage.tpl", cities = cities)



@app.route("/<city>/")
def showFondCityPage(city):
  streets = db.session.query(distinct(Client.streetName)).filter_by(cityName = city).order_by(Client.streetName.asc()).all()
  return render_template("fond/showCityPage.tpl", city = city, streets = streets)



@app.route("/<city>/<street>/")
def showFondStreetPage(city, street):
  houses = db.session.query(distinct(Client.houseNumber)).filter_by(cityName = city, streetName = street).order_by(Client.houseNumber.asc()).all()
  return render_template("fond/showFondStreetPage.tpl", city = city, street = street, houses = houses)



@app.route("/<city>/<street>/<house>/")
def showFondHousePage(city, street, house):
  clients = Client.query.filter_by(cityName = city, streetName = street, houseNumber = house).order_by(Client.flatNumber.asc()).all()
  return render_template("fond/showFondHousePage.tpl", city = city, street = street, house = house, clients = clientsSchema.dump(clients).data)



@app.route("/client/<clientId>/")
def showFondClientPage(clientId):
  client = Client.query.get_or_404(clientId)
  return render_template("fond/showFondClientPage.tpl", client = clientSchema.dump(client).data)



@app.route("/client/<clientId>/generatePassword/")
def showGeneratePasswordPage(clientId):
  client = Client.query.get_or_404(clientId)
  return render_template("fond/showGeneratePasswordPage.tpl", client = client)



@app.route("/client/<clientId>/generatePassword/", methods = ["post"])
def generatePassword(clientId):
  client = Client.query.get_or_404(clientId)
  password = uuid4().hex[:6]
  client.setPasswordHash(Client.generateHash(password))
  db.session.commit()
  sendEmail.delay(client.email, "Востановление пароля от личного кабинета", recoveryPhrase.format(client.number[:-2], client.number[-2:], password, current_app.config["SITE_URL"]))
  return render_template("fond/successGeneratePassword.tpl", client = client)



@app.route("/client/<clientId>/edit/")
def showFondClientEditPage(clientId):
  client = Client.query.get_or_404(clientId)
  return render_template("fond/showFondClientEditPage.tpl", client = client)



@app.route("/client/<clientId>/edit/", methods=["post"])
def updateClientInfo(clientId):
  client = Client.query.get_or_404(clientId)

  # смена лицевого счета
  number = request.form.get("number", None)
  if number and number != client.getNumber():
    exist = Client.query.filter_by(number = number).one_or_none()
    if exist:
      raise RuntimeError("Такой лицевой счет принадлежит другому абоненту.")
    else:
      client.setNumber(number)

  # смена всех остальных параметров
  client.setCityName(request.form["cityName"])
  client.setStreetName(request.form["streetName"])
  client.setHouseNumber(request.form["houseNumber"])
  client.setFlatNumber(request.form["flatNumber"])
  client.setFio(request.form["fio"])
  client.setTelephone(request.form["telephone"])
  client.setEmail(request.form["email"])
  client.setDebt(request.form["debt"])
  client.setPenalty(request.form["penalty"])
  db.session.commit()
  return redirect("/fond/client/{}/".format(client.getId()))



@app.route("/client/<clientId>/metrics/")
def showFondClientMetricsPage(clientId):
  client = Client.query.get_or_404(clientId)
  pus = [pu.id for pu in client.pus]
  metrics = Metric.query.filter(Metric.puId.in_(pus)).order_by(Metric.month.desc()).all()
  client = clientSchema.dump(client).data
  metrics = metricsSchema.dump(metrics).data
  return render_template("fond/showFondClientMetricsPage.tpl", client = client, metrics = metrics, datetime = datetime)