from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# initialize app
app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

app.config.from_object(Config)

# give it a database (for now using sqlite)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# flow control extensions for templates
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

from app.admin.controllers import admin
from app.main.controllers import main

# separate admin portal from regular users
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

from app.util import models

# shell stuff to make development easier
from app import app, db
from app.util.models import User, Post
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}