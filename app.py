from flask import Flask
from config.database import DevelopmentConfig
import config.constants as const
from utils.database import db
from utils.schema import ma
from utils.migrate import migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    app.secret_key = const.SECRET_KEY
    app.template_folder = const.TEMPLATES_FOLDER
    app.debug = True
    app.static_folder = const.STATICFILES_FOLDER
    

    db.init_app(app=app)
    ma.init_app(app=app)
    migrate.init_app(app=app, db=db)

    return app


app = create_app()