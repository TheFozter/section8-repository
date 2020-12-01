import sqlite3
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_refresh_token_required, 
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
)
from models.user import UserModel
from blacklist import BLACKLIST

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
    type=str,
    required=True,
    help="This field cannot be blank!"
)
_user_parser.add_argument('password',
    type=str,
    required=True,
    help="This field cannot be blank!"
)

class UserRegister(Resource):

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']) is not None:
            return {"message": "User name '{}' already exists!".format(data['username'])}, 400
        
        user = UserModel(**data)
        user.save_to_db()

<<<<<<< HEAD
        return {"message": "User created successfully."}, 201
    
class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        
        if not user:
            return {'message': "User not found."}, 404
        return user.json()
    
    @classmethod
    def delete(cls, user_id):
        user  = UserModel.find_by_id(user_id)
        
        if not user:
            return {'message': "User not found."}, 404
        user.delete_from_db()
        return {'message': "User deleted."}, 200
    
class UserLogin(Resource):
    @classmethod
    def post(cls):
        # get data from parser
        data = _user_parser.parse_args()
        
        # find user in database
        user = UserModel.find_by_username(data['username'])
        
        # check password
        # this is what the `authenticate()` function user to do
        if user and safe_str_cmp(user.password, data['password']):
            # identity = is what the `identity()` function used to do
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        return {'message': 'Invalid credentials.'}, 401
        # create access token
        # create refresh token (we will look this later!)
        # return them

class UserLogout(Resource):
     @jwt_required
     def post(self):
        jti = get_raw_jwt()['jti'] #jti is "JWT ID", a unique identifier for a JWT
        BLACKLIST.add(jti)
        return {'message': 'Successfully logged out.'}, 200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
=======
        return {"message": "User created successfully."}, 201
>>>>>>> eeb050a6c2083b1828c79657bf7314a95d6c18db
