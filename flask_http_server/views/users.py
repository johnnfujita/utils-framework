from werkzeug.security import generate_password_hash, check_password_hash
from flask_http_server.server import db
from flask import request, jsonify
from flask_http_server.models.users import Users, user_schema, users_schema


def post_user():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return (
            jsonify({"message": "User created successfully.", "data": result.data}),
            201,
        )
    except:
        return (
            jsonify({"message": "An error occurred creating the user.", "data": {}}),
            500,
        )
