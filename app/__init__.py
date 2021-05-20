from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
from datetime import timedelta

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.permanent_session_lifetime = timedelta(minutes=5)
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
        
    
    return app