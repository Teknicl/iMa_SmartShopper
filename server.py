from flask_app import app
from flask_app.controllers import users, lists

if __name__ == "__main__":
    app.run(debug=True)