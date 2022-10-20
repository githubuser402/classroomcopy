import datetime
from types import ClassMethodDescriptorType

import jwt
from itsdangerous import URLSafeTimedSerializer

from config.constants import Constants


class Token:
    __const = Constants()
    @classmethod
    def encode(cls, slug):
        token_data = {
            "slug": slug, 
            "exp": datetime.datetime.now() + cls.__const.TOKEN_LIFE_TIME 
            }
        token = jwt.encode(token_data, cls.__const.SECRET_KEY, cls.__const.ALGORITHM)
        return token

    @classmethod
    def decode(cls, token):
        try:
            token_data = jwt.decode(token, cls.__const.SECRET_KEY, algorithms=[cls.__const.ALGORITHM,])
            return token_data
        except Exception as ex:
            raise ex


class VerificationToken:
    __const = Constants()
    @classmethod
    def encode(cls, email):
        serializer = URLSafeTimedSerializer(cls.__const.SECRET_KEY)
        return serializer.dumps(email, salt=cls.__const.SECURITY_PASSWORD_SALT)

    @classmethod
    def decode(cls, token, expiration=3600):
        serializer = URLSafeTimedSerializer(cls.__const.SECRET_KEY)

        try:
            email = serializer.loads(token, salt=cls.__const.SECURITY_PASSWORD_SALT, max_age=expiration)
        except Exception as ex:
            return ex
        return email