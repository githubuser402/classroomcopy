from flask import Blueprint, request
from utils.response import response_with
import utils.response as resp
from config.constants import Constants
from models.user_model import User, UserSchema
import datetime
import jwt
import uuid


user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=['POST'])
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
        user.slug = uuid.uuid4[:20]
        user.save()

        token_data = {"slug": user.slug, "exp": datetime.datetime.now() + Constants.token_life_time}
        token = jwt.encode(token_data, Constants.secret_key, Constants.algorithm)
        
        print(token)

        return response_with(resp.SUCCESS_201, value={"token": token})

    except Exception as ex:
        print(ex)
        return response_with(resp.CONFLICT_409)


@user_routes.route("/login", methods=["POST"])
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

    token_data = {"slug": user.slug , "exp": datetime.datetime.now() + Constants.token_life_time}
    token = jwt.encode(token_data, Constants.secret_key, Constants.algorithm)

    return response_with(resp.SUCCESS_200, value={"token": token})     