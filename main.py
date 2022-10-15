from app import app
from routes.admin_class_routes import admin_class_routes
from routes.core_routes import core_routes
from routes.student_class_routes import student_class_routes
from routes.user_routes import user_routes
from utils.database import db

app.register_blueprint(core_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/api/u/')
app.register_blueprint(student_class_routes, url_prefix='/api/s/c/')
app.register_blueprint(admin_class_routes, url_prefix='/api/a/c/')

if __name__ == "__main__":
    app.run()