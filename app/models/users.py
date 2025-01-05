import bcrypt

from app import db

salt = bcrypt.gensalt()


class Users(db.Model):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user, must be unique and not null.
        password (str): The hashed password of the user, must be unique and not null.

    Properties:
        senhacrip (str): Property to get the hashed password.

    Methods:
        senhacrip.setter: Sets the hashed password using bcrypt.
        converte_senha(senha_texto_claro: str) -> bool: Checks if the provided plain text password matches the stored hashed password.
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=60), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False, unique=True)

    @property
    def senhacrip(self):
        return self.senhacrip

    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.password = bcrypt.hashpw(senha_texto.encode(), salt).decode("utf-8")

    def converte_senha(self, senha_texto_claro) -> bool:
        return bcrypt.checkpw(
            senha_texto_claro.encode("utf-8"), self.password.encode("utf-8")
        )
