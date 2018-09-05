from .celery import celery
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from dbf import Table
from app.domain import Client, Metric, PU
from datetime import datetime
from app.ext import db



# не стал выносить в конфиг
host = "smtp.mail.ru"
email = "example_kch@mail.ru"
password = "example"


@celery.task
def sendEmail(to, theme, text):
  try:
    msg = MIMEText(text)
    msg["Subject"] = theme
    msg["From"] = email
    msg["to"] = to
    with SMTP_SSL(host) as smtp:
      smtp.login(email, password)
      smtp.send_message(msg)
  except Exception as e:
    pass



def searchPU(pus, order, service):
  """
    Поиск счетчика в переданном массиве
  """
  order = order.strip()
  service = service.strip()
  for pu in pus:
    if pu.order == order and pu.service == service:
      return pu
  return None



@celery.task
def importMetrics(file, importMetricsFlag):
  existedPUs = {}
  table = Table(file)
  try:
    table.open()

    clients = {}
    for row in table:
      number, notUse1, notUse2, notUse3, notUse4, notUse5, notUse6, notUse7, service, notUse8, order, serial, date, m1, m1n, m2, m2n = row
      if number in clients:
        client = clients[number]
      else:
        client = Client.query.filter_by(number = number).one_or_none()
        clients[number] = client

      if client:
        # загружаю все счетчики разово по лицевому счету
        if number not in existedPUs:
          pus = PU.query.filter_by(client = client).all()
          existedPUs[number] = pus

        # если счетчик найден удаляю его из списка существующих
        # после завершения импорта все оставшиеся счетчики и их показания в этом словаре будут удалены
        pu = searchPU(existedPUs[number], order, service)
        if pu:
          pu.setSerial(serial)
          existedPUs[number].remove(pu)
        else:
          pu = PU(client, order, service, serial)
          db.session.add(pu)
        # если в форме указано импортировать показания то помимо импорта счетчиков импортируются и показания
        if importMetricsFlag:
          print("Импорт показаний")
          date = datetime.strptime(date, "%d.%m.%Y")
          m = Metric.query.filter_by(pu = pu, month = date.strftime("%Y%m")).one_or_none()
          if not m:
            m = Metric(pu, date, m1, m2)
            db.session.add(m)
          m.setM(m1, m2)

    # удаление счетчиков которые есть в базе, но нет в импортируемом файле
    for pus in existedPUs.values():
      for pu in pus:
        db.session.delete(pu)
    db.session.commit()
  finally:
    table.close()



@celery.task
def importLsAndDebt(file):
  table = Table(file)
  try:
    table.open()
    for row in table:
      number, city, street, dom, building, flat, room, fio, debt, penalty, notUse1, notUse2, payDate = row
      client = Client.query.filter_by(number = number).one_or_none()
      if not client:
        client = Client(number, city, street, dom, building, flat, room, fio)
      client.setDebt(debt)
      client.setPenalty(penalty)
      client.setPayDate(payDate)
      db.session.add(client)
    db.session.commit()
  finally:
    table.close()
