from . import db

# userd class that will define all the different users
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index = True)
    email = db.Column(db.String(250), unique=True, index=True)

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
