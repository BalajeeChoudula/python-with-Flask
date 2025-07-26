
from app.routes import routes
from flask import Flask
def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    for route in routes:
        app.register_blueprint(route)
    
    return app