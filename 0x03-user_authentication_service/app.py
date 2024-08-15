#!/usr/bin/env python3
"""a basic Flask app.
"""
from flask import Flask, jsonify, abort, request, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'])
def index() -> str:
    """Display a greeting message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Register a new user in the database"""
    try:
        user_email = request.form['email']
        user_password = request.form['password']
    except KeyError:
        abort(400)
    try:
        new_user = AUTH.register_user(user_email, user_password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": user_email, "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Handle POST request to initiate a new user session."""
    user_data = request.form
    if "email" not in user_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in user_data:
        return jsonify({"message": "password required"}), 400
    else:
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        if AUTH.valid_login(user_email, user_password) is False:
            abort(401)
        else:
            user_session_id = AUTH.create_session(user_email)
            login_response = jsonify({
                "email": user_email,
                "message": "logged in"})
            login_response.set_cookie('session_id', user_session_id)
            return login_response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def log_out() -> None:
    """Ends the session for the user associated with the given session ID."""
    session_token = request.cookies.get('session_id')
    account = AUTH.get_user_from_session_id(session_token)
    if not account:
        abort(403)
    AUTH.destroy_session(account.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Retrieve the user associated with the session ID and return a 200 status if found."""
    session_token = request.cookies.get('session_id')
    account = AUTH.get_user_from_session_id(session_token)
    if account:
        return jsonify({"email": account.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """Handle POST request to generate a password reset token."""
    try:
        user_email = request.form["email"]
    except KeyError:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(user_email)
    except ValueError:
        abort(403)
    return jsonify({"email": user_email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """Handle the PUT request to update the user's password."""
    try:
        email = request.form["email"]
        reset_token = request.form["reset_token"]
        new_password = request.form["new_password"]
    except KeyError:
        abort(400)
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
