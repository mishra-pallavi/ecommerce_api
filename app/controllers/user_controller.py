from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    # Logic to retrieve and return users from the database
    users = [{"id": 1, "name": "User 1"}, {"id": 2, "name": "User 2"}]
    return jsonify(users)

# Additional routes and controller logic can be added here
