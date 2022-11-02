from flask import Blueprint, request, url_for, current_app

import utils.response as resp
from app import db
from models.class_model import Class, ClassSchema
from models.task_model import Task, TaskSchema
from models.user_model import User
from models.document_model import Document
from utils.decorators import token_required
from utils.response import response_with

from utils.document_filter import is_allowed_file
from werkzeug.utils import secure_filename
from config.constants import Constants

import os


student_class_routes = Blueprint("class_routes", __name__)

#classes
@student_class_routes.route("/", methods=["GET"])
@token_required
def get_classes_list(user):
    
    classes = db.session.query(Class).filter(Class.students.any(User.id == user.id)).all()
    
    if not classes:
        return response_with(resp.SERVER_ERROR_404)

    class_schema = ClassSchema(many=True)
    classes_json = class_schema.dump(classes)
    return response_with(resp.SUCCESS_200, value=classes_json)


@student_class_routes.route("/<class_public_id>/", methods=["GET"])
@token_required
def get_class(user, class_public_id):
    class_ = db.session.query(Class).filter(Class.students.any(User.id == user.id), Class.public_id == class_public_id).first() 

    if not class_:
        return response_with(resp.SERVER_ERROR_404)

    class_schema = ClassSchema()
    class_json = class_schema.dump(class_)
    return response_with(resp.SUCCESS_200, value=class_json)



#tasks
@student_class_routes.route("/<class_public_id>/t/", methods=['GET'])
@token_required
def get_task_list(user, class_public_id):
    class_ = Class.query.filter_by(public_id=class_public_id).first()
    
    if not class_:
        return response_with(resp.SERVER_ERROR_404, message="Class does not esist")
    
    tasks = db.session.query(Task).filter_by(class_id=class_public_id).filter(user in class_.students).all()

    task_schema = TaskSchema(many=True)
    tasks_json = task_schema.dump(tasks)

    return response_with(resp.SUCCESS_200, value=tasks_json)


@student_class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['GET'])
@token_required
def get_task(user, class_public_id, task_public_id):
    class_ = Class.query.filter_by(public_id=class_public_id).first()

    if not class_:
        return response_with(resp.SERVER_ERROR_404)
    
    task = db.session.query(Task).filter_by(class_id=class_public_id).filter(user in class_.students).filter_by(public_id=task_public_id).first()

    if not task:
        return response_with(resp.SERVER_ERROR_404, message="Task does not exist")
    
    task_schema = TaskSchema()
    task_json = task_schema.dump(task)

    return response_with(resp.SUCCESS_200, value=task_json)   


@student_class_routes.route("/<class_public_id>/t/<task_public_id>/", methods=['PATCH'])
@token_required
def add_material(user, class_public_id, task_public_id):
    class_ = Class.query.filter_by(public_id=class_public_id).first()
    if not class_:
        return response_with(resp.SERVER_ERROR_404)
    
    task = db.session.query(Task).filer_by(class_id=class_public_id).filter(user in class_.students).filter_by(public_id=task_public_id).first()

    if not task:
        return response_with(resp.SERVER_ERROR_404, message="Task does not exist") 
        #do later 

    
@student_class_routes.route("/<class_public_id>/t/<task_public_id>/d/", methods=["POST"])
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

        document.path = url_for("uploaded_file", filename=filename, _extermal=True)
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

