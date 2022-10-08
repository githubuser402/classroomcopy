from traceback import print_tb
from flask import Blueprint, jsonify, request, make_response, redirect, url_for
from utils.response import response_with
import utils.response as resp
from config.constants import Constants
from models.user_model import User
import datetime
import jwt


user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/login", methods=['POST'])
def user_registration():
    data = {item[0]: item[1] for item in request.form.items()}
    print(type(data))
    data['password'] = User.generate_hash(data['password'])
    print(data)
    user = User(**data)
    user.save()
    token_data = {"name": user.username, "exp": datetime.datetime.now() + datetime.timedelta(minutes=45)}
    token = jwt.encode(token_data, Constants.secret_key, Constants.algorithm)

    redir = redirect(url_for("core_routes.classes_list"))
    redir.headers.add("access_token", token)
    
    return redir