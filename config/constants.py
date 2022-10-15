import datetime
import os
from os import path
from pathlib import Path


class Constants:
    class TokenLifeTime:
        __seconds = 0
        __minutes = 0
        __hours = 2
        __days = 0

        def __call__(self):
            return datetime.timedelta(days=self.__days, hours=self.__hours, minutes=self.__minutes, seconds=self.__seconds)

    __template_folder = path.join(Path(__file__).parent.parent, "templates")
    __staticfiles_folder = path.join(Path(__file__).parent.parent, "static")
    __algorithm = "HS256"
    __token_life_time = TokenLifeTime()

    @classmethod
    @property
    def secret_key(cls):
        if not os.environ.get("SECRET_KEY"):
            raise Exception("environment variable SECRET_KEY is not provided!")
        
        return os.environ['SECRET_KEY']

    @classmethod
    @property
    def security_password_salt(cls):
        if not os.environ.get("SECURITY_PASSWORD_SALD"):
            raise Exception("environment variable SECURITY_PASSWORD_SALD is not provided")

        return os.environ["SECURITY_PASSWORD_SALD"]

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

    @classmethod
    @property
    def token_life_time(cls):
        return cls.__token_life_time()