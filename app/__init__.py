from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_user:your_password@localhost:5432/task_manager'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.db import init_db
    init_db(app)
    print("APP adn db initialized")
    
    # Register routes
    from app.routes import task_routes
    app.register_blueprint(task_routes)

    return app
