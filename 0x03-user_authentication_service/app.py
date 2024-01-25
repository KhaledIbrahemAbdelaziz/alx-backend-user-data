#!/usr/bin/env python3
""" Route module for the API """

from flask import Flask, jsonify, request,  abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /status
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """ POST /users
    Return:
      - message
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
