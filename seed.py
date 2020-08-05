from app import app
from models import db, User

db.drop_all()
db.create_all()
User.query.delete()

u1 = User(
    username="test1",
    password="test1",
    first_name="test1_firstname",   
    last_name="test1_lastname",
    email="test1@gmail.com",
)

u2 = User(
    username = "test2",
    password = "test2",
    first_name = "test2_firstname",   
    last_name = "test2_lastname",
    email = "test2@gmail.com",
)

u3 = User(
    username = "test3",
    password = "test3",
    first_name = "test3_firstname",   
    last_name = "test3_lastname",
    email = "test3@gmail.com",
)

db.session.add_all([u1, u2, u3])
db.session.commit()