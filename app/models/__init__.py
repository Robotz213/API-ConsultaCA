from app import app, db
from app.misc.gen_seed import generate_id
from app.models.ca import CaTable
from app.models.users import Users

"""
This module initializes the database and creates a default root user if it does not exist.

Imports:
    app (Flask): The Flask application instance.
    db (SQLAlchemy): The SQLAlchemy database instance.
    generate_id (function): Function to generate a unique ID.
    CaTable (class): The CA table model.
    Users (class): The Users table model.

Attributes:
    __all__ (list): List of public objects of that module, as interpreted by import *.

Functionality:
    - Creates all database tables defined in the models.
    - Checks if a user with the username "root" exists.
    - If the "root" user does not exist, it generates a password, creates the user, and commits the user to the database.
    - Prints the generated password for the "root" user.
"""

__all__ = ["CaTable", "Users"]

with app.app_context():

    db.create_all()

    usr = Users.query.filter(Users.username == "root").first()
    if not usr:

        pw = generate_id()
        user = Users(username="root", senhacrip=pw)

        db.session.add(user)
        db.session.commit()

        print(f" * Password: {pw}")
