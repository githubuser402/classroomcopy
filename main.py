from app import app
from routes.core import core_routes
from routes.user import user_routes
from routes.task import task_routes
from utils.database import db


app.register_blueprint(core_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/api/users/')
app.register_blueprint(task_routes, url_prefix='/api/tasks/')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run()