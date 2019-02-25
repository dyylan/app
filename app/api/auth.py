from flask import jsonify, request
from flask_jwt_extended import create_access_token
from . import api
from ..models import User
from .. import jwt


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'role': user.role_id}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username:
        user = User.query.filter_by(username=username).first()
    if email:
        user = User.query.filter_by(email=email).first()
    if user.verify_password(password):
        token = create_access_token(identity=user)
        api_token = {'access_token': token}
        return jsonify(api_token), 200
    return jsonify({"Message": "Username or password is wrong"}), 401
