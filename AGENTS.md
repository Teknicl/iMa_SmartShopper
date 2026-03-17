# AGENTS.md

## Project Overview
- `iMa_SmartShopper` is a small Flask + MySQL shopping list app.
- The entrypoint is `server.py`, which imports the Flask app plus the route modules and runs with `debug=True`.
- Dependencies are managed with Pipenv. The declared runtime stack is Python `3.12`, `flask`, `pymysql`, and `flask-bcrypt`.

## Repository Layout
- `server.py`: app entrypoint.
- `flask_app/__init__.py`: Flask app creation and `secret_key`.
- `flask_app/controllers/`: route handlers for users and shopping-list actions.
- `flask_app/models/`: database access and validation logic.
- `flask_app/config/mysqlconnection.py`: low-level MySQL connector wrapper.
- `flask_app/templates/`: Jinja templates.
- `flask_app/static/`: CSS and images.
- `ima_smartshopper.mwb`: MySQL Workbench schema file.

## Local Setup
1. Install dependencies with `pipenv install`.
2. Make sure a local MySQL server is running.
3. Create/import the `ima_smartshopper` database. The schema appears to live in `ima_smartshopper.mwb`.
4. The app currently expects MySQL credentials in code:
   - host: `localhost`
   - user: `root`
   - password: `root`
5. Start the app with `pipenv run python server.py`.

## How The App Works
- Unauthenticated users land on `/`.
- `users.py` handles registration, sign-in, and sign-out.
- `lists.py` handles shopping-list views plus create/edit/update/delete item flows.
- Session-based auth is used through `session["user_id"]`.
- Models combine validation and SQL execution; this codebase does not currently separate services/forms from models.

## Agent Conventions
- Preserve the existing Flask MVC-ish structure:
  - routes in `flask_app/controllers`
  - SQL and validation in `flask_app/models`
  - templates in `flask_app/templates`
- Keep changes small and consistent with the current style unless the task explicitly calls for refactoring.
- When adding routes, import any new controller modules from `server.py` so they register.
- When adding database-backed features, keep the database name aligned with the current constant: `ima_smartshopper`.
- Prefer matching existing template flow and URL patterns over introducing new abstractions.

## Known Constraints
- There is no automated test suite in the repository right now.
- Database credentials and the Flask secret key are hardcoded; avoid silently changing this behavior unless the task is specifically about configuration/security improvements.
- The code uses table names `user` and `list`, which are easy to confuse with Python built-ins and SQL reserved words. Be careful when editing related queries.
- Some current validation and naming are inconsistent. Preserve user-visible behavior unless the task is to fix it.

## Recommended Validation After Changes
- Run `pipenv run python server.py` to confirm the app boots.
- Manually verify:
  - register/sign-in/sign-out
  - viewing the shopping list
  - adding, editing, and deleting list items
- If a change touches SQL, verify it against a local MySQL database instead of assuming template-only correctness.

## High-Risk Files
- `flask_app/config/mysqlconnection.py`: affects every database call.
- `flask_app/models/user.py`: registration/authentication logic.
- `flask_app/models/list.py`: CRUD logic for shopping-list items.
- `flask_app/controllers/lists.py`: session checks and route flow.
