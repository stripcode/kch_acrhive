from app import createAdminApp
from app.ext import db
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", dest = "config", required = True)
args = parser.parse_args()

app = createAdminApp(args.config)
app.app_context().push()
db.drop_all()