from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from datetime import datetime
from dataclasses import dataclass

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@dataclass
class User(db.Model):
    __tablename__ = "users"

    id:int
    username : str
    password : str
    passwordEncrypt : str
    lastTimeConnection : str

    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    passwordEncrypt = db.Column(db.String(150), unique=True, nullable=True)
    lastTimeConnection = db.Column(db.String(50), default='', nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.passwordEncrypt = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.passwordEncrypt, password)


@app.route("/")
def help():
    return jsonify([
        {"url": "/api/v1.0/signup", "method": "POST", "request": "{\"username\": \"root\", \"password\": \"toor\"}"}, 
        {"url": "/api/v1.0/signin", "method": "POST", "request": "{\"username\": \"root\", \"password\": \"toor\"}"}, 
        {"url": "/api/v1.0/users", "method": "GET", "response": "{\"users\": [{\"id\": 1,\"lastTimeConnection\": \"11-25-2020 19:30:36\",\"password\": \"toor\",\"passwordEncrypt\": \"$2b$12$y4HcdCLfFS7F1vKpKhH3b.JJFQougKyb0sfgj/DFsb9b/hLWJe0nS\",\"username\": \"root\"}"}, 
    ]), 200

@app.route("/api/v1.0/signup", methods=["POST"])
def signup():
    if not request.json:
        abort(400)
    user_exist = User.query.filter_by(username=request.json.get('username', '')).first()
    if user_exist:
        return jsonify({"result": "El usuario ya se encuentra registrado"}), 201

    user = User(request.json.get('username', '') , request.json.get('password', ''))
    db.session.add(user)
    db.session.commit()
    return jsonify({"result": "El usuario ha sido registrado"}), 200

@app.route("/api/v1.0/signin", methods=["POST"])
def signin():
    if not request.json:
        abort(400)
    user = User.query.filter_by(username=request.json.get('username', '')).first()
    if user.is_correct_password(request.json.get('password', '')):
        user.lastTimeConnection = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        db.session.commit()
        return jsonify({"result": "El usuario y la contraseña son correctos"}), 200
    else:
        return jsonify({"result": "El usuario y/o la contraseña son invalidos"}), 404

@app.route("/api/v1.0/users", methods=["GET"])
def get_users():
    if not request.json:
        abort(400)
    users = User.query.all()
    return jsonify({'users': users}), 200