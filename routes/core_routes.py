from flask import Blueprint, request, render_template

core_routes = Blueprint("core_routes", __name__)


@core_routes.route('/', methods=["GET"])
def classes_list():
    return render_template("core/index.html")


@core_routes.route('/<public_id>', methods=['GET'])
def class_details(public_id):
    return render_template("core/discipline_details.html", public_id=public_id)


@core_routes.route('/login/', methods=['GET'])
def login():
    return render_template("core/login.html")
