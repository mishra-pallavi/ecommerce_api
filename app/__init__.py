from flask import Flask
from config import settings

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Load configuration from settings module
    app.config.from_object(settings)

    # Register blueprints (if you have multiple controllers)
    from app.controllers.product_controller import product_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(product_bp)
    app.register_blueprint(user_bp)

    # Additional setup and configurations can be added here

    return app
