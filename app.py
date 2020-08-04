'''Flask app for Notes'''

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User
from forms import AddUserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """Redirect to register."""

    return redirect('/register')

@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Show form to register/create user."""

    form = AddUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data   
        email = form.email.data 
        first_name = form.first_name.data
        last_name = form.last_name.data

        flash(f"{username} register!")

        user = User.register(username=username, password=password, email=email,
                        first_name=first_name, last_name=last_name)
        
        db.session.add(user)
        db.session.commit()

        return redirect("/secret")
    
    else:
        return render_template("add_user_form.html", form=form)

