from flask import Blueprint, render_template, request, current_app, redirect, url_for
import os
from werkzeug.utils import secure_filename
from app.tasks import importMetrics, importLsAndDebt
from app.celery import celery


app = Blueprint('Import', __name__)



@app.route("/LsAndPeni/")
def showImportLsAndPeni():
  return render_template("import/showImportLsAndPeni.tpl")



@app.route("/LsAndPeni/", methods = ["post"])
def importLsAndPeni():
  if "file" not in request.files:
    return "Нет файла"
  file = request.files['file']
  if file.filename == '':
    return 'No selected file'
  filename = secure_filename(file.filename)
  fullpath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
  file.save(fullpath)
  result = importLsAndDebt.delay(fullpath)
  return redirect(url_for("Import.resultImportLsAndDebt", resultId = result.id))



@app.route("/LsAndPeni/<resultId>")
def resultImportLsAndDebt(resultId):
  result = celery.AsyncResult(resultId)
  return render_template("import/resultImportLsAndDebt.tpl", result = result)



@app.route("/metrics/")
def showMetricsImportForm():
  return render_template("import/showMetricsImportForm.tpl")



@app.route("/metrics/", methods = ["post"])
def postImportMetrics():
  if "file" not in request.files:
    return "Нет файла"
  file = request.files['file']
  if file.filename == '':
    return 'No selected file'

  filename = secure_filename(file.filename)
  fullpath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
  file.save(os.path.join(fullpath))
  result = importMetrics.delay(fullpath, request.form.get("yes", False))
  return redirect(url_for("Import.resultImportMetrics", resultId = result.id))



@app.route("/metrics/<resultId>")
def resultImportMetrics(resultId):
  result = celery.AsyncResult(resultId)
  return render_template("import/resultImportMetrics.tpl", result = result)