from app import app
from routes.core import core_routes

app.register_blueprint(core_routes, url_prefix='/')

if __name__ == "__main__":
    app.run()