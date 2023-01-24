from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    valid_user = User.create_valid_user(request.form)
    print(valid_user)
    if not valid_user:
        return redirect('/')
    session['user_id'] = valid_user.id
    return redirect('/shopping_list')

@app.route('/login',methods=['POST'])
def login():
    valid_user = User.authenticated_user_by_input(request.form)
    if not valid_user:
        return redirect('/')
    session["user_id"] = valid_user.id
    return redirect('/shopping_list')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')