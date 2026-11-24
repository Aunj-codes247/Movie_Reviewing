from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class user(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = True)
   
    email = db.Column(db.String(100), unique = True , nullable = True)

    # learning password hassing 

    hash_password = db.Column(db.String(158))
    @property
    def password(self):
        raise AttributeError('password is not a readble atrribute ')

    
    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)
class save(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    movie_id = db.Column(db.String(24), nullable = True)
    user_id = db.Column(db.Integer, nullable = True)
    Rating = db.Column(db.Integer, nullable = True)
