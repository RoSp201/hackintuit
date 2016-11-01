import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #for the database
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

import sys
sys.path.append('/home/robert/side_projects/hackintuit/Data/')
import csvMaker
jobs = cm.jobs.values()
print jobs

app = Flask(__name__)

#enter configuration information for CSRF with Flask-WTF extension
app.config.from_object('config')

#initialize the database
database = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'


from app import views, models













