from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    from app.models import Task
    db.init_app(app)
    with app.app_context():
        print("Database being created...!")
        db.create_all()
        print("Database initialized!")
