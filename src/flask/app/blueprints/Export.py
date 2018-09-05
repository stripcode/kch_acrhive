from flask import Blueprint, render_template, request, current_app, send_file
from datetime import datetime
from app.ext import db
from app.domain import serviceNames, months
from dbf import Table
import os

selectQuery = "SELECT client.id, client.cityName, client.streetName, client.houseNumber, client.buildingName, client.flatNumber, client.room, client.fio,  client.number, pu.service, pu.id, pu.order, pu.serial, metric.month, metric.time, \
metric.m  FROM metric, pu, client WHERE metric.month = {month} and pu.id = metric.puId and pu.clientId = client.id order by metric.time"



app = Blueprint('Export', __name__)




@app.route("/")
def showExportPage():
  return render_template("export/showExportPage.tpl")



@app.route("/", methods = ["post"])
def viewExportMetrics():
  monthDateStr = request.form.get("monthDate", None)
  if not monthDateStr:
    raise RuntimeError("Месяц не задан.")
  month = datetime.strptime(monthDateStr, "%m.%Y")
  metrics = db.session.execute(selectQuery.format(month = month.strftime("%Y%m"))).fetchall()

  if "view" in request.form:
    return render_template("export/viewExportMetrics.tpl", metrics = metrics, serviceNames = serviceNames, datetime = datetime, months = months)
  else:
    fullname = os.path.join(current_app.config['UPLOAD_FOLDER'], "export.dbf")
    columns = "code_ls C(7); np C(20); st C(30); dom C(4); korp C(7); kw C(9); komn C(9); abonent C(30); s_code C(2); s_name C(25); code_nn C(2); sn C(20); date C(10); quan1 C(15); quan1n C(15); quan2 C(15); quan2n C(15)"
    table = Table(fullname, columns, codepage = "cp866")
    try:
      table.open()
      for row in metrics:
        m1, m2 = row.m.split(";")
        table.append((row.number, row.cityName, row.streetName, row.houseNumber, row.buildingName, row.flatNumber, row.room, row.fio, row.service, serviceNames[row.service], row.order, row.serial, datetime.fromtimestamp(row.time).strftime("%d.%m.%Y"), "", m1, "", m2))
    finally:
      table.close()
    return send_file(fullname, as_attachment = True)