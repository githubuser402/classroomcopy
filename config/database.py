from pathlib import Path
import os

DATABASE_NAME = "school.db"

class DevelopmentConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{os.path.join(Path(__file__).parent.parent, DATABASE_NAME)}"   


class DevelopmentConfigMySQL:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"""mysql+mysqldb://{os.environ.get('MYSQL_ADMIN_USERNAME')}:{os.environ.get('MYSQL_ADMIN_PASSWORD')}@localhost/{os.environ.get('MYSQL_DB_NAME')}"""