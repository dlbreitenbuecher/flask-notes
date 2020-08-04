'''Models for Notes'''

from flask_sqlalchemy import SQLAlchemy  
from flask_bcrypt import Bcrypt 

db = SQLAlchemy()
bcrypt = Bcrypt()


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


    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register user with hashed password and return user."""

        hashed = bcrypt.generate_password_hash(password).decode("utf8")

        #return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed, first_name=first_name, 
                                last_name=last_name, email=email)


    @classmethod
    def authenticate(cls, username, password):
        '''Validate user exists and password is correct.
        Return user if valid; else return False
        '''
        
        # TODO: ask if we could also write user = cls.query...
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False