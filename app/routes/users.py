from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app import mongo
from app.schemas import UserSchema
from app.utils.password import hash_password

user_bp = Blueprint('users', __name__)
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    data["password"] = hash_password(data["password"])
    result = mongo.db.users.insert_one(data)
    return jsonify({"id": str(result.inserted_id)}), 201

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    users = list(mongo.db.users.find())
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
        del user["password"]
    return jsonify(users), 200

@user_bp.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    user["id"] = str(user["_id"])
    del user["_id"]
    del user["password"]
    return jsonify(user), 200

@user_bp.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    if "password" in data:
        data["password"] = hash_password(data["password"])

    result = mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User updated"}), 200

@user_bp.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200