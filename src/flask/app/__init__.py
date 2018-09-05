from flask import Flask
from flask_login import LoginManager
from .ext import db
from .domain import Client, User



def createCeleryApp():
  app = Flask(__name__)
  app.config.from_pyfile("config.default.py")
  app.config.from_envvar("KCH_PRODUCTION", silent = True)
  db.init_app(app)
  return app



def createAdminApp():
  app = Flask(__name__, template_folder = "admin_templates", static_url_path = "/static", static_folder = "admin_static")
  app.config.from_pyfile("config.default.py")
  app.config.from_envvar("KCH_PRODUCTION", silent = True)
  db.init_app(app)

  # настройка аутентификации
  login_manager = LoginManager()
  login_manager.login_view = "AdminPage.showLoginForm"
  @login_manager.user_loader
  def load_user(clientId):
    user = User()
    user.is_active = True
    user.is_authenticated = True
    return user
  login_manager.init_app(app)
  from .blueprints.AdminPage import app as AdminPage
  from .blueprints.Fond import app as Fond
  from .blueprints.Import import app as Import
  from .blueprints.Export import app as Export

  app.register_blueprint(AdminPage)
  app.register_blueprint(Fond, url_prefix = "/fond")
  app.register_blueprint(Import, url_prefix = "/import")
  app.register_blueprint(Export, url_prefix = "/export")
  return app



def createClientApp():
  app = Flask(__name__, template_folder = "client_templates", static_url_path = "/static", static_folder = "client_static")
  app.config.from_pyfile("config.default.py")
  app.config.from_envvar("KCH_PRODUCTION", silent = True)
  db.init_app(app)

  from .blueprints.ClientPage import app as ClientPage

  # настройка аутентификации
  login_manager = LoginManager()
  login_manager.login_view = "ClientPage.showLoginForm"
  @login_manager.user_loader
  def load_user(clientId):
    user = Client.query.filter_by(id = clientId).one_or_none()
    if user:
      user.is_active = True
      user.is_authenticated = True
    return user
  login_manager.init_app(app)
  app.register_blueprint(ClientPage)
  return app