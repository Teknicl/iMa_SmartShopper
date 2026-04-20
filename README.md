# iMa SmartShopper

iMa SmartShopper is a Flask and MySQL shopping list web app. Users can register, sign in, and manage a personal shopping list with item names, categories, notes, and quantities.

## Features

- User registration and sign-in with hashed passwords using Flask-Bcrypt
- Session-based authentication
- Per-user shopping list view
- Create, edit, update, and delete shopping list items
- Server-side validation with flash messages
- MySQL/MariaDB-backed data storage

## Tech Stack

- Python 3.12
- Flask
- PyMySQL
- Flask-Bcrypt
- MySQL or MariaDB
- Jinja templates
- HTML/CSS

## Project Structure

```text
.
├── server.py
├── Pipfile
├── ima_smartshopper.sql
├── ima_smartshopper.mwb
└── flask_app
    ├── __init__.py
    ├── config
    │   └── mysqlconnection.py
    ├── controllers
    │   ├── lists.py
    │   └── users.py
    ├── models
    │   ├── list.py
    │   └── user.py
    ├── static
    │   ├── css
    │   └── img
    └── templates
        ├── create.html
        ├── edit.html
        ├── index.html
        └── shopping_list.html
```

## Local Setup

1. Install Pipenv if needed:

   ```bash
   pip install pipenv
   ```

2. Install project dependencies:

   ```bash
   pipenv install
   ```

3. Make sure MySQL or MariaDB is running locally.

4. Create the database from the included SQL file:

   ```bash
   mysql -uroot -proot < ima_smartshopper.sql
   ```

   If your local root password is different, adjust the command accordingly.

5. Confirm the database connection settings in `flask_app/config/mysqlconnection.py`:

   ```python
   host = 'localhost'
   user = 'root'
   password = 'root'
   db = db
   ```

6. Start the Flask app:

   ```bash
   pipenv run python server.py
   ```

7. Open the local development URL shown in the terminal, usually:

   ```text
   http://127.0.0.1:5000
   ```

## Database

The app uses the `ima_smartshopper` database with two main tables:

- `user`: stores account information and hashed passwords
- `list`: stores shopping list items associated with a user

The schema is available in both:

- `ima_smartshopper.sql`
- `ima_smartshopper.mwb`

## Main Routes

- `GET /`: registration and sign-in page
- `POST /register`: create a new user account
- `POST /signin`: sign in an existing user
- `GET /signout`: clear the current session
- `GET /shopping_list`: view the signed-in user's shopping list
- `GET /item/add`: show the add-item form
- `POST /shopping_list`: create a shopping list item
- `GET /item/edit/<list_id>`: show the edit-item form
- `POST /item/update/<list_id>`: update an item
- `GET /item/delete/<list_id>`: delete an item

## Notes

- The app currently stores database credentials directly in `flask_app/config/mysqlconnection.py`.
- There is no automated test suite in this repository yet.
- The app expects a local MySQL/MariaDB server and the `ima_smartshopper` database to exist before running.
