from ast import Constant
from config.constants import Constants
import datetime
import jwt

class Token:
    @staticmethod
    def encode(slug):
        token_data = {
            "slug": slug, 
            "exp": datetime.datetime.now() + Constants.token_life_time
            }
        token = jwt.encode(token_data, Constants.secret_key, Constants.algorithm)
        return token

    @staticmethod
    def decode(token):
        try:
            token_data = jwt.decode(token, Constants.secret_key, algorithms=[Constants.algorithm,])
            return token_data
        except Exception as ex:
            raise ex