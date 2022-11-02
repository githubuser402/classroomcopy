from flask import Blueprint

import utils.response as resp
from app import db
from models.document_model import Document
from models.task_model import Task, TaskSchema
from models.user_model import User
from utils.decorators import token_required
from utils.response import response_with


document_route = Blueprint("document_routes", __name__)


@document_route("/", methods=['POST'])
@token_required
def get_document(user):
    pass