import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#configure database
app.config['SECRET_KEY'] = '\xf7g\xd7`\x08f\xc1\xeer\x00)\xa0#r\xad\x07\xb0\xc9:\xc6\xccZ\xa1>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
db = SQLAlchemy(app)

#configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.init_app(app)

#enable debugtoolbar
app.debug = True
toolbar = DebugToolbarExtension(app)


#for displaying timestamps
moment = Moment(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from .bookmarks import bookmarks as bookmarks_blueprint
app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')

from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')

import models
#import views
