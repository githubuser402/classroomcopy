from flask import Flask

from config.constants import Constants
from config.database import DevelopmentConfigMySQL
from models.class_model import Class
from models.task_model import Task
from models.user_model import User
from utils.database import db
from utils.migrate import migrate
from utils.schema import ma


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfigMySQL)
    
    const = Constants()

    app.secret_key = const.SECRET_KEY
    app.template_folder = const.TEMPLATE_FOLDER
    app.debug = True
    app.static_folder = const.STATICFILES_FOLDER
    

    db.init_app(app=app)
    ma.init_app(app=app)
    migrate.init_app(app=app, db=db)

    return app


app = create_app()