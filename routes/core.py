from flask import Blueprint, request, render_template

core_routes = Blueprint("core_routes", __name__)

@core_routes.route('/', methods=["GET"])
def core():
    return render_template("core/index.html")


@core_routes.route('/login/', methods=['GET'])
def login():
    return render_template("core/login.html")