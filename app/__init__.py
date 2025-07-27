
from app.routes import routes
from flask import Flask
def create_app():
    # Create the Flask application
    app = Flask(__name__)
    
    # Register blueprints
    for route in routes:
        app.register_blueprint(route)

    return app
