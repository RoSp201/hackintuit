#part of sqlachlemy database building
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#required by the Flask-SQLAlchemy extension
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#the folder where we will store the SQLAlchemy-migrate data files.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



#used for login id validation
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

