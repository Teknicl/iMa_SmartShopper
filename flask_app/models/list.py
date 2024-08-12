from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

db = "ima_smartshopper"
class List:
    def __init__(self, list):
        self.id = list["id"]
        self.item = list["item"]
        self.category = list["category"]
        self.note = list["note"]
        self.qty = list["qty"]
        self.created_at = list["created_at"]
        self.updated_at = list["updated_at"]
        self.user = None

    @classmethod
    def get_all(cls):
        query = """SELECT 
                    list.id, list.created_at, list.updated_at, item, category, note, qty,
                    user.id as user_id, firstname, lastname, username, email, password, user.created_at as uc, user.updated_at as uu
                    FROM list
                    JOIN user on user.id = list.user_id;"""
        list_data = connectToMySQL(db).query_db(query)
        lists = []
        for list in list_data:
            print (list_data)
            list_obj = cls(list)
            list_obj.user = user.User(
                {
                    "id": list["user_id"],
                    "firstname": list["firstname"],
                    "lastname": list["lastname"],
                    "username": list["username"],
                    "email": list["email"],
                    "password": list["password"],
                    "created_at": list["uc"],
                    "updated_at": list["uu"],
                }
            )
            lists.append(list_obj)
        return lists

    @classmethod
    def create_valid_list(cls, list_dict):
        if not cls.is_valid(list_dict):
            return False
        query = "INSERT INTO list (item, category, note, qty, user_id) VALUES (%(item)s, %(category)s, %(note)s, %(qty)s, %(user_id)s);"
        list_id = connectToMySQL(db).query_db(query, list_dict)
        list = cls.get_by_id(list_id)
        return list

# Show users shopping list by id
    @classmethod
    def create_user_list(cls, user_id):
        data = {"id": user_id}
        query = """SELECT 
                    list.id, list.created_at, list.updated_at, item, category, note, qty,
                    user.id as user_id, firstname, lastname, username, email, password, user.created_at as uc, user.updated_at as uu
                    FROM list
                    JOIN user on user.id = list.user_id
                    WHERE user_id = %(id)s;"""
        list_data = connectToMySQL(db).query_db(query,data)
        lists = []
        for list in list_data:
            list_obj = cls(list)
            list_obj.user = user.User(
                {
                    "id": list["user_id"],
                    "firstname": list["firstname"],
                    "lastname": list["lastname"],
                    "username": list["username"],
                    "email": list["email"],
                    "password": list["password"],
                    "created_at": list["uc"],
                    "updated_at": list["uu"],
                }
            )
            lists.append(list_obj)
        return lists

    @classmethod
    def get_by_id(cls, list_id):
        data = {"id": list_id}
        query = """SELECT list.id, list.created_at, list.updated_at, list.item, list.category, list.note, list.qty, user.id as user_id, user.firstname, user.lastname, user.username, user.email, user.password, user.created_at as uc, user.updated_at as uu
        FROM list
        JOIN user on user.id = list.user_id
        WHERE list.id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        result = result[0]
        list = cls(result)
        list.user = user.User(
                {
                    "id": result["user_id"],
                    "firstname": result["firstname"],
                    "lastname": result["lastname"],
                    "username": result["username"],
                    "email": result["email"],
                    "password": result["password"],
                    "created_at": result["uc"],
                    "updated_at": result["uu"]
                }
            )           
        return list

    @classmethod
    def delete_list_by_id(cls, list_id):
        data = {"id": list_id}
        query = "DELETE from list WHERE id = %(id)s;"
        connectToMySQL(db).query_db(query, data)
        return list_id
    
    @classmethod
    def update_list(cls, list_id):
        if not cls.is_valid(list_id):
            return False
        query = "UPDATE list SET item = %(item)s, category = %(category)s, note = %(note)s, qty = %(qty)s WHERE id = %(id)s;"
        connectToMySQL(db).query_db(query, list_id)
        list = cls.get_by_id(list_id["id"])
        return list

    @staticmethod
    def is_valid(list_dict):
        valid = True
        flash_string = " field is required and must be at least 2 characters."
        print(list_dict)
        if len(list_dict["item"]) < 2:
            flash("Item " + flash_string)
            valid = False
        return valid