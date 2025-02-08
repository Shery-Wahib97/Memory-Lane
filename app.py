from flask import Flask, request, jsonify, session
import os
from flask_cors import CORS
# from werkzeug.security import generate_password_hash, check_password_hash
from classes import Users

class_data = Users()

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

########################################## LOGIN
@app.route('/api/login', methods=['POST'])
def login():
    user_login = request.get_json()
    username = user_login.get('username')
    password = user_login.get('password')

    # if not username or not password:
    #     return jsonify({"Error": "Username and password are required"}), 401

    users = class_data.load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            session["username"] = username
            return jsonify({"message": "Login Successfuly", "username" : username }), 200
    return jsonify({"Error": "Invalid Username or password"}), 401


###################################### REGISTER
@app.route("/api/register", methods = ["POST"])
def register():
    users = class_data.load_users()

    user_id = 1 if not users else max(user["id"] for user in users) + 1

    new_user = request.get_json()
    new_user["id"] = user_id
    firstname = new_user["firstname"]
    lastname = new_user["lastname"]
    username = new_user["username"]
    password = new_user["password"]

    if not firstname or not lastname or not username or not password :
        return jsonify({"error": "All fields must be entered"}), 400
    
    if any(user["username"] == username for user in users):
        return jsonify({"error": "This Username already exists"}), 401
    
    users.append({
        "id": user_id,
        "firstname": firstname,
        "lastmame": lastname,
        "username": username,
        "password": password
    })
    class_data.save_users(users)
    return jsonify({"message": "egistration successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)