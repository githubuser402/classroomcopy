from flask import Flask
from config.database import DevelopmentConfigMySQL
from config.constants import Constants
from utils.database import db
from utils.schema import ma
from utils.migrate import migrate

from models.class_model import Class
from models.task_model import Task
from models.user_model import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfigMySQL)
    
    app.secret_key = Constants.secret_key
    app.template_folder = Constants.template_folder
    app.debug = True
    app.static_folder = Constants.staticfiles_folder
    

    db.init_app(app=app)
    ma.init_app(app=app)
    migrate.init_app(app=app, db=db)

    return app


app = create_app()