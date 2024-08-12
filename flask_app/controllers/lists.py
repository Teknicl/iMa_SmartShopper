from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.list import List
from flask import flash

@app.route("/shopping_list")
def shopping_list():
    if "user_id" not in session:
        flash("You must be signed in to access your shopping list.", "Signin")
        return redirect("/")

    user = User.get_user_id(session["user_id"])
    list = List.create_user_list(session["user_id"])
    return render_template("shopping_list.html", user=user, list=list)

@app.route("/shopping_list/<int:list_id>")
def list(list_id):
    user = User.get_user_id(session["user_id"])
    list = List.get_by_id(list_id)
    return render_template("shopping_list.html", user=user, list=list)

@app.route("/item/add")
def list_create_page():
    user = User.get_user_id(session["user_id"])
    return render_template("create.html", user=user)

@app.route("/item/edit/<int:list_id>")
def list_edit_page(list_id):
    if "user_id" not in session:
        flash("You must be signed in to edit items.", "Signin")
        return redirect("/")
    user = User.get_user_id(session["user_id"])
    list = List.get_by_id(list_id)
    return render_template("edit.html", user=user, list=list)

@app.route("/item/update/<int:list_id>", methods=["POST"])
def update_list(list_id):
    if "user_id" not in session:
        flash("You must be signed in to update items.", "Signin")
        return redirect("/")
    valid_list = List.is_valid(request.form)
    if valid_list:
        List.update_list(request.form)
        return redirect(f'/shopping_list')
    return redirect(f'/item/edit/{list_id}')

@app.route("/shopping_list", methods =["POST"])
def create_list():
        valid_list = List.create_valid_list(request.form)
        if valid_list:
            return redirect(f'/shopping_list')
        return redirect(f'/item/add')

@app.route("/item/delete/<int:list_id>")
def delete_by_id(list_id):
    if "user_id" not in session:
        flash("You must be signed in to delete itmes from your list.", "Signin")
        return redirect("/")
    List.delete_list_by_id(list_id)
    return redirect("/shopping_list")