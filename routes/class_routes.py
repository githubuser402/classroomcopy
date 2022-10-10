from operator import methodcaller
from flask import Blueprint
from utils.response import response_with
import utils.response as resp
from models.class_model import Class, ClassSchema
from models.task_model import Task, TaskSchema


class_routes = Blueprint("class_routes", __name__)

#classes
@class_routes.route("/", methods=["GET"])
def get_classes_list():
    return ''


@class_routes.route("/<class_public_id>/", methods=["GET"])
def get_class(class_public_id):
    return '' 


@class_routes.route("/<class_public_id>/", methods=["POST"])
def cleate_class(class_public_id):
    return ''


@class_routes.route("/<class_public_id>/", methods=["PATCH"])
def edit_class(class_public_id):
    return ''


@class_routes.route("/<class_public_id>/", methods=["DELETE"])
def delete_class(class_public_id):
    return ''



#tasks
@class_routes.route("/<class_public_id>/t/", methods=['GET'])
def get_task_list():
    return ''


@class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['GET'])
def get_task(class_public_id, task_public_id):
    return ''


@class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['POST'])
def create_task(class_public_id, task_public_id):
    return ''


@class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['PATCH'])
def edit_task(class_public_id, task_public_id):
    return ''


@class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['DELETE'])
def delete_task(class_public_id, task_public_id):
    return ''