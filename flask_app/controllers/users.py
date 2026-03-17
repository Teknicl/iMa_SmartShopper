from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    register_form = session.pop("register_form", {})
    signin_form = session.pop("signin_form", {})
    return render_template(
        "index.html",
        register_form=register_form,
        signin_form=signin_form,
    )

@app.route('/register', methods=['POST'])
def register():
    valid_user = User.create_valid_user(request.form)
    print(valid_user)
    if not valid_user:
        session["register_form"] = {
            "firstname": request.form.get("firstname", ""),
            "lastname": request.form.get("lastname", ""),
            "username": request.form.get("username", ""),
            "email": request.form.get("email", ""),
        }
        return redirect('/')
    session['user_id'] = valid_user.id
    return redirect('/shopping_list')

@app.route('/signin',methods=['POST'])
def signin():
    valid_user = User.authenticated_user_by_input(request.form)
    if not valid_user:
        session["signin_form"] = {
            "username": request.form.get("username", ""),
        }
        return redirect('/')
    session["user_id"] = valid_user.id
    return redirect('/shopping_list')

@app.route('/signout')
def signout():
    session.clear()
    return redirect('/')
