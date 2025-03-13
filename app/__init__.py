from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Ensure User model is correctly imported
        return User.query.get(int(user_id))
    
    
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.blog import blog_bp
   
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    

    return app
