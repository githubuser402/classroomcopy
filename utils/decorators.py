from flask import request, redirect, url_for
from config.constants import Constants
from models.user_model import User
from app import app 
from functools import wraps
import jwt


def token_required(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.has_key("x-access-token"):
            return redirect(url_for("login"))
        
        token = request.headers.get("x-access-token")
        
        try:
            token_data = jwt.decode(token, key=Constants.secret_key, algorithms=[Constants.algorithm,])
            print(token_data)
        except Exception as ex:
            return redirect(url_for("login"))

        return func(*args, **kwargs)
    return wrapper