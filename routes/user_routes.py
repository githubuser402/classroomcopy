import uuid

from flask import Blueprint, request

import utils.response as resp
from config.constants import Constants
from models.user_model import User, UserSchema
from utils.response import response_with
from utils.token import Token

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register/", methods=['POST'])
def user_registration():
    data = request.get_json()
    user_schema = UserSchema()
    
    try:
        cleared_data = user_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)

    cleared_data['password'] = User.generate_hash(data['password'])

    try:
        user = User(**cleared_data)
        user.slug = uuid.uuid4().hex[:20]
        user.save()

        token = Token.encode(slug=user.slug)
        
        return response_with(resp.SUCCESS_201, value={"token": token})

    except Exception as ex:
        print(ex)
        return response_with(resp.CONFLICT_409)


@user_routes.route("/login/", methods=["POST"])
def user_login():
    data = request.get_json()
    user_schema = UserSchema()

    try: 
        cleared_data = user_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)

    user =  User.query.filter_by(username=cleared_data['username']).first()

    if not user:
        return response_with(resp.SERVER_ERROR_404, message="user does not exist")

    if not User.verify_hash(user.password, cleared_data['password']):
        return response_with(resp.INVALID_INPUT_422, message="password is wrong")

    token = Token.encode(slug=user.slug)

    return response_with(resp.SUCCESS_200, value={"token": token})     