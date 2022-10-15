import datetime
from random import expovariate

import jwt
from itsdangerous import URLSafeTimedSerializer

from config.constants import Constants


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


class VerificationToken:
    @staticmethod
    def encode(email):
        serializer = URLSafeTimedSerializer(Constants.secret_key)
        return serializer.dumps(email, salt=Constants.security_password_salt)

    @staticmethod
    def decode(token, expiration=3600):
        serializer = URLSafeTimedSerializer(Constants.secret_key)

        try:
            email = serializer.loads(token, salt=Constants.security_password_salt, max_age=expiration)
        except Exception as ex:
            return ex
        return email