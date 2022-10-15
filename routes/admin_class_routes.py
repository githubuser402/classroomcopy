import uuid

from flask import Blueprint, request

import utils.response as resp
from app import db
from models.class_model import Class, ClassSchema
from models.task_model import Task, TaskSchema
from models.user_model import User
from utils.decorators import token_required
from utils.response import response_with

admin_class_routes = Blueprint("admin_class_routes", __name__)

@admin_class_routes.route("/", methods=["GET"])
@token_required
def list_admined_classes(user):
    admined_classes = db.session.query(Class).filter(Class.admin_users.any(User.id == user.id)).all()
    class_schema = ClassSchema(many=True)

    admined_classes_json = class_schema.dump(admined_classes)

    return response_with(resp.SUCCESS_200, value=admined_classes_json)


@admin_class_routes.route("/", methods=["POST"])
@token_required
def create_class(user):
    data = request.get_json()
    class_schema = ClassSchema()

    try:
        cleared_data = class_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)
    
    class_ = Class(**cleared_data)
    class_.public_id = uuid.uuid4().hex[:10]
    user.administred_classes.append(class_)
    class_.save()
    user.save() 

    return response_with(resp.SUCCESS_201, message="Class was successfully created")


@admin_class_routes.route("/<class_public_id>/", methods=["PATCH"])
@token_required
def edit_class(user, class_public_id):
    data = request.get_json()
    class_schema = ClassSchema()
    
    try:
        cleared_data = class_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)
    
    class_ = db.session.query(Class).filter(Class.admin_users.any(User.id == user.id)).filter_by(public_id=class_public_id).first()

    if not class_:
        return response_with(resp.SERVER_ERROR_404, message="Class does not esist")
    
    class_.name = cleared_data.get("name", class_.name)
    class_.description = cleared_data.get("description", class_.description)
    class_.save()

    return response_with(resp.SUCCESS_200, value=class_schema.dump(class_))


@admin_class_routes.route("/<class_public_id>/", methods=["DELETE"])
def delete_class(class_public_id):
    return ''


@admin_class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['PATCH'])
def edit_task(class_public_id, task_public_id):
    return ''


@admin_class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['DELETE'])
def delete_task(class_public_id, task_public_id):
    return ''


@admin_class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['POST'])
def create_task(class_public_id, task_public_id):
    return ''