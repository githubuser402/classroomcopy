from pathlib import Path
from os import path
import os


class Constants:
    __template_folder = path.join(Path(__file__).parent.parent, "templates")
    __staticfiles_folder = path.join(Path(__file__).parent.parent, "static")
    __algorithm = "HS256"

    @classmethod
    @property
    def secret_key(cls):
        if not os.environ.get("SECRET_KEY"):
            raise Exception("environment variable SECRET_KEY is not provided!")
        
        return os.environ['SECRET_KEY']

    @classmethod
    @property
    def template_folder(cls):
        return cls.__template_folder

    @classmethod
    @property
    def staticfiles_folder(cls):
        return cls.__staticfiles_folder

    @classmethod
    @property
    def algorithm(cls):
        return cls.__algorithm