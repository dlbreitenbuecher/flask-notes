'''Models for Notes'''

from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()

def connect_db(app):
    '''Connect to database'''

    db.app = app
    db.init_app(app)   


class User(db.Model):
    '''User.'''

    ___tablename__ = 'users'

    username = db.Column(db.String(20),
                        primary_key=True,
                        unique = True)
    password = db.Column(db.String,
                        nullable = False)
    email = db.Column(db.String(50),
                        nullable = False,
                        unique=True)
    first_name = db.Column(db.String(30),
                            nullable=False)
    last_name = db.Column(db.String(30),
                            nullable=False)

    def __repr__(self):
        '''Show user instance information'''

        return f'''<username {self.username}, 
        first_name {self.first_name}, last_name {self.last_name}>'''

    