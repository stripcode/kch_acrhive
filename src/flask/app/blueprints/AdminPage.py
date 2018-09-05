from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required
from app.domain import User, Client
from app.tasks import sendEmail



app = Blueprint('AdminPage', __name__)

messageTemplate = """
Уважаемый {fio}, Вам, поступило информационное сообщение для лицевого счета №{number} из личного кабинета УЖК "Наш дом".
Вы можете войти в личный кабинет по ссылке {site}.

{message}
"""


@app.route("/")
@login_required
def defaultPrivatePage():
  return render_template("defaultPrivatePage.tpl")



@app.route("/enter/")
def showLoginForm():
  return render_template("enter.tpl")



@app.route("/enter/", methods = ["post"])
def loginUser():
  login = request.form.get('login', "")
  password = request.form.get('password', "")
  if login in current_app.config["USERS"] and password == current_app.config["USERS"][login]:
    user = User()
    user.is_active = True
    user.is_authenticated = True
    login_user(user)
  return redirect(url_for('AdminPage.defaultPrivatePage'))



@app.route("/logout/")
@login_required
def logout():
  logout_user()
  return redirect(url_for('AdminPage.showLoginForm'))



@app.route("/email/")
@login_required
def showEmailPage():
  return render_template("email.tpl")



@app.route("/email/", methods = ["post"])
@login_required
def processEmailPage():
  message = request.form.get("message", None)
  if message:
    clients = Client.query.filter(Client.email != "").all()
    for client in clients:
      msg = messageTemplate.format(fio = client.fio, number = client.number, site = current_app.config["SITE_URL"], message = message)
      sendEmail.delay(client.email, "Информационное сообщение от УЖК Наш дом", msg)
  return render_template("email_success.tpl")