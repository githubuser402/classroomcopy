from ssl import VERIFY_DEFAULT
from urllib import response
from flask import Blueprint
from utils.response import response_with
import utils.response as resp
from models.task_model import Task
from models.class_model import Class

task_routes = Blueprint("task_routes", __name__)

@task_routes.route("/", methods=['GET'])
def get_tasks():
    return response_with(resp.SUCCESS_200, value={"tasks": {"span": "eggs"}})


@task_routes.route("/<public_id>", methods=['GET'])
def get_task(public_id):
    task_json = None
    return response_with(resp.SUCCESS_200, value={"task": task_json})