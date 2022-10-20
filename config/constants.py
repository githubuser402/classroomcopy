import datetime
import os
from dataclasses import dataclass
from os import path
from pathlib import Path


@dataclass
class Constants:
    class _TokenLifeTime:
        __seconds = 0
        __minutes = 0
        __hours = 2
        __days = 0

        def default_token(self):
            return datetime.timedelta(days=self.__days, hours=self.__hours, minutes=self.__minutes, seconds=self.__seconds)


    @property
    def SECRET_KEY(self):
        if not os.environ.get("SECRET_KEY"):
            raise Exception("environment variable SECRET_KEY is not provided!")
        
        return os.environ['SECRET_KEY']

    @property
    def SECURITY_PASSWORD_SALT(self):
        if not os.environ.get("SECURITY_PASSWORD_SALD"):
            raise Exception("environment variable SECURITY_PASSWORD_SALD is not provided")

        return os.environ["SECURITY_PASSWORD_SALD"]

    @property
    def TOKEN_LIFE_TIME(self):
       return self._TokenLifeTime().default_token()

    TEMPLATE_FOLDER = path.join(Path(__file__).parent.parent, "templates")
    STATICFILES_FOLDER = path.join(Path(__file__).parent.parent, "static")
    ALGORITHM = "HS256"
    