from pathlib import Path
import os

DATABASE_NAME = "school.db"

class DevelopmentConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{os.path.join(Path(__file__).parent.parent, DATABASE_NAME)}"   