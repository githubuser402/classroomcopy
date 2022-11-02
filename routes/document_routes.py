from flask import Blueprint, request, url_for, send_from_directory

import utils.response as resp
from app import db
from models.document_model import Document
from models.task_model import Task, TaskSchema
from models.class_model import Class
from models.user_model import User
from utils.decorators import token_required
from utils.response import response_with

from utils.document_filter import is_allowed_file
from werkzeug.utils import secure_filename
from config.constants import Constants

import os

document_routes = Blueprint("document_routes", __name__)


@document_routes.route("/<class_public_id>/t/<task_public_id>/d/", methods=["POST"])
@token_required
def upload_document(user, class_public_id, task_public_id):
    try:
        file = request.files['student_document']

        if file and not is_allowed_file(file.content_type):
            return response_with(resp.INVALID_INPUT_422, message="Document has invalid extension")

        filename = secure_filename(file.filename)
        file.save(os.path.join(Constants.MEDIAFILES_FOLDER, filename))

        # class_ = Class.query.filter_by(public_id=class_public_id).first()

        if not Class.query.filter_by(public_id=class_public_id).first():
            return response_with(resp.SERVER_ERROR_404, message="class doesnt exist")

        task = Task.query.filter_by(task_id=task_public_id).first()
        if not task:
            return response_with(resp.SERVER_ERROR_404, message="task doesnt exist")

        document = Document()

        document.path = url_for("get_document", filename=filename, _extermal=True)
        document.task_id = task.id
        document.user_id = user.id
        
        user.student_documents.append(document)
        
        document.save()
        user.save()
        
        task_schema = TaskSchema()
        task_json =  task_schema.dump(task)

        return response_with(resp.SUCCESS_201, value=task_json)

    except Exception as ex:
        return response_with(resp.INVALID_INPUT_422)


@document_routes.route("/<filename>", methods=['GET'])
def get_document(filename):
    return send_from_directory(Constants.MEDIAFILES_FOLDER, filename)