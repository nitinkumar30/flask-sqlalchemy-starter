from flask import Blueprint
from app import db
from models import User

main = Blueprint('main', __name__)


@main.route('/create_user/<name>')
def create_user(name):
    user = User(username=name)
    db.session.add(user)
    db.session.commit()
    return f"User {name} created"
