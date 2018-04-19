from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin


# userd class that will define all the different users
class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index = True)
    email = db.Column(db.String(250), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))      #User authentication


        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)



def __repr__(self):
        return f'User {self.username}'


# Role class that will define all the different roles
class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String)
    user = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return f'User {self.name}'
