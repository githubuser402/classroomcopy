from app import app
from routes.core_routes import core_routes
from routes.user_routes import user_routes
from routes.class_routes import class_routes
from utils.database import db


app.register_blueprint(core_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/api/u/')
app.register_blueprint(class_routes, url_prefix='/api/c/')

if __name__ == "__main__":
    # with app.app_context():
        # db.create_all()
        
    app.run()