SQLALCHEMY_DATABASE_URI =  "mysql+pymysql://kch:Aa123456@localhost/kch_dev"
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = '/Users/nekrasov/sites/tmp'
ALLOWED_EXTENSIONS = set(['dbf'])
SECRET_KEY = "example"
SITE_URL = "https://lk.example.ru"
CELERY_BROKER_URL = "redis://localhost"
CELERY_RESULT_BACKEND = "redis://localhost"
SBER_LOGIN = "EXAMPLE"
SBER_PASSWORD = "EXAMPLE"
SBER_RETURN_URL = "http://localhost:5000/pay/success/"
USERS = {
  "admin": "Aa123456"
}