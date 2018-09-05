from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta



db = SQLAlchemy()



def getValidMonth():
  now = datetime.now()
  mday = int(now.strftime("%d"))
  if mday > 25:
    now = now + timedelta(days = 10)
  return now