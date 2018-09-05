from .ext import db
from hashlib import sha1
from datetime import datetime
import re

mPattern = re.compile("^([0-9]*\.[0-9]{2})[0-9]*$")

serviceNames = {
  "06": "Холодное водоснабжение",
  "20": "Горячее водоснабжение",
  "11": "Электроэнергия"
}

months = {
  "01": "январь",
  "02": "февраль",
  "03": "март",
  "04": "апрель",
  "05": "май",
  "06": "июнь",
  "07": "июль",
  "08": "август",
  "09": "сентябрь",
  "10": "октябрь",
  "11": "ноябрь",
  "12": "декабрь",
}

recoveryPhrase = "Для пользователя с лицевым счетом {}-{} для личного кабинета жителя сгенерирован следующий пароль {}\n\
Адресс личного кабинета {}"

# Класс лицевого счета
class Client(db.Model):
  __tablename__ = "client"
  id = db.Column(db.Integer, primary_key = True)
  cityName = db.Column(db.String(255), nullable = False)
  streetName = db.Column(db.String(255), nullable = False)
  houseNumber = db.Column(db.String(255), nullable = False)
  buildingName = db.Column(db.String(255), nullable = False)
  flatNumber = db.Column(db.String(255), nullable = False)
  room = db.Column(db.String(255), nullable = False)
  number = db.Column(db.String(255), nullable = False, unique=True)
  fio = db.Column(db.String(255), nullable = False)
  telephone = db.Column(db.String(255), nullable = False)
  email = db.Column(db.String(255), nullable = False)
  password = db.Column(db.String(255), nullable = False)
  debt = db.Column(db.String(255), nullable = False)
  penalty = db.Column(db.String(255), nullable = False)
  penalty = db.Column(db.String(255), nullable = False)
  payDate = db.Column(db.String(255), nullable = False)

  pus = db.relationship("PU", back_populates="client", order_by = (db.desc("pu.order"), db.asc("pu.service")))

  def __init__(self, number, cityName, streetName, houseNumber, buildingName, flatNumber, room, fio):
    self.setNumber(number)
    self.setCityName(cityName)
    self.setStreetName(streetName)
    self.setHouseNumber(houseNumber)
    self.setBuildingName(buildingName)
    self.setFlatNumber(flatNumber)
    self.setRoom(room)
    self.setFio(fio)
    self.telephone = ""
    self.email = ""
    self.password = ""
    self.debt = 0
    self.penalty = 0
    self.payDate = ""

  # Метод нужен для flask_login
  def get_id(self):
    return self.getId()

  def getId(self):
    return self.id

  def getNumber(self):
    return self.number

  def setPasswordHash(self, password):
    self.password = password.strip()

  def setNumber(self, number):
    number = number.strip()
    if number == "":
      raise RuntimeError("Лицевой счет не валиден")
    self.number = number

  def setCityName(self, cityName):
    cityName = cityName.strip()
    if cityName == "":
      raise RuntimeError("Название города не валидно")
    self.cityName = cityName

  def setStreetName(self, streetName):
    streetName = streetName.strip()
    if streetName == "":
      raise RuntimeError("Название улицы не валидно")
    self.streetName = streetName

  def setHouseNumber(self, houseNumber):
    houseNumber = houseNumber.strip()
    if houseNumber == "":
      raise RuntimeError("Номер дома не валиден")
    self.houseNumber = houseNumber

  def setBuildingName(self, buildingName):
    self.buildingName = buildingName.strip()

  def setFlatNumber(self, flatNumber):
    self.flatNumber = flatNumber.strip()

  def setRoom(self, room):
    self.room = room.strip()

  def setPayDate(self, payDate):
    self.payDate = payDate.strip()

  def setTelephone(self, telephone):
    self.telephone = telephone.strip()

  def setEmail(self, email):
    self.email = email.strip()

  def setFio(self, fio):
    self.fio = fio.strip()

  def setDebt(self, debt):
    self.debt = debt

  def setPenalty(self, penalty):
    self.penalty = penalty

  def generateHash(password):
    return sha1(password.encode("utf8")).hexdigest()



class PU(db.Model):
  __tablename__ = "pu"
  id = db.Column(db.Integer, primary_key = True)
  serial = db.Column(db.String(255), nullable = False)
  order = db.Column(db.String(255), nullable = False, index = True)
  service = db.Column(db.String(255), nullable = False, index = True)

  # привзка клиента
  clientId = db.Column(db.Integer, db.ForeignKey('client.id'))
  client = db.relationship("Client", back_populates="pus")

  # привязка показаний
  metrics = db.relationship("Metric", back_populates="pu", cascade="all", order_by = "Metric.month")

  def __init__(self, client, order, service, serial):
    self.setClient(client)
    self.setOrder(order)
    self.setService(service)
    self.setSerial(serial)

  def getService(self):
    return self.service

  def setOrder(self, order):
    order = order.strip()
    if order not in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]:
      raise RuntimeError("Порядковый номер не валиден")
    self.order = order

  def setService(self, service):
    service = service.strip()
    if service not in ["06", "20", "11"]:
      raise RuntimeError("Услуга не валидна")
    self.service = service

  def setSerial(self, serial):
    serial = serial.strip()
    self.serial = serial

  def setClient(self, client):
    if not isinstance(client, Client):
      raise RuntimeError("Клиент не валиден")
    self.client = client



class Metric(db.Model):
  __tablename__ = "metric"
  id = db.Column(db.Integer, primary_key = True)
  time = db.Column(db.Integer, nullable = False, index = True)
  month = db.Column(db.String(6), nullable = False, index = True)
  m = db.Column(db.String(255), nullable = False)

  # привзяка прибора
  puId = db.Column(db.Integer, db.ForeignKey('pu.id'))
  pu = db.relationship("PU", back_populates = "metrics")

  # не давать менять повторно ни date параметры
  # т.к. не будут консистентны выгрузки
  # да и житель скажет "чего вы мои показания изменели"
  def __init__(self, pu, date, m1, m2):
    if not isinstance(date, datetime):
      raise RuntimeError("Дата не валидна")
    if not isinstance(pu, PU):
      raise RuntimeError("Счетчик не валиден")
    self.pu = pu
    self.setM(m1, m2)
    self.month = date.strftime("%Y%m")
    self.time = date.timestamp()

  def setM(self, m1, m2):
    m1re = mPattern.match(m1.strip())
    m2re = mPattern.match(m2.strip())
    m1 = m1re.group(1) if m1re else "0.00"
    m2 = m2re.group(1) if m2re else "0.00"
    self.m = ";".join([m1, m2])



class User():

  def __init__(self):
    self.name = "Админ"

  def get_id(self):
    return 1