from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "ima_smartshopper"
    def __init__(self, data):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        @classmethod
        def save(cls, data):
            query = "INSERT INTO user { firstname, lastname, username, email, password) VALUES (%(firstname)s, %(lastname)s, %(username)s, %(email)s, %(password)s);"
            return connectToMySQL(cls.db).query_db(query, data)

        @classmethod
        def get_user_id(cls, data):
            query = "SELECT * FROM user WHERE id = %(id)s;"
            result = connectToMySQL(cls.db).query_db(query, data)
            return cls(result[0])

        @classmethod
        def get_user_username(cls, data):
            query = "SELECT * FROM user WHERE usernmae = %(username)s;"
            result = connectToMySQL(cls.db).query_db(query, data)
            pass