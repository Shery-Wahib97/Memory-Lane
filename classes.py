import json
from flask import jsonify

class Users:
    def __init__(self, user_file_path = "users.json"):
        self.user_file_path = user_file_path

################# Load And Save user Data In Json File

    def load_users(self):
        try:
            with open (self.user_file_path, "r") as reading:
                return json.load(reading)
        except json.JSONDecodeError:
            return []

    def save_users(self, memory):
        with open(self.user_file_path, "w") as writing:
            json.dump(memory, writing, indent=4)

################# Register User