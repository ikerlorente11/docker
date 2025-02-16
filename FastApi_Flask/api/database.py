import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

user = os.getenv("MYSQL_USER", "default_user")
password = os.getenv("MYSQL_PASSWORD", "default_password")
database = os.getenv("MYSQL_DATABASE", "default_database")
host = "db"

flask_app = Flask(__name__)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"

# Init database
db = SQLAlchemy()
db.init_app(flask_app)
migrate = Migrate(flask_app, db)

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))

# SEEDERS
def seed():
    # Comprobar si ya existen usuarios en la base de datos
    if not User.query.first():
        user1 = User(firstName="John", lastName="Doe")
        user2 = User(firstName="Jane", lastName="Smith")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        print("Datos de prueba insertados correctamente.")

if __name__ == "__main__":
    with flask_app.app_context():
        seed()