'''Flask app for Notes'''

from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import AddUserForm, LoginForm
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)
# app.config['SECRET_KEY'] = "very-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

debug = DebugToolbarExtension(app)

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



@app.route('/login', methods=['GET', 'POST'])
def login_user():
    '''Produce login form or handle login'''

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username=username, password=password)
        print('user', user)
        
        if user:
            session['user_id'] = user.username
            # 'success' is a flash category. We can use this to style our flash messages. 
            # 'success' refers to a bootstrap keyword, e.g. alert-success 
            flash(f'{user.username} logged in!', 'success')
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Incorrect Username or Password']
    
    return render_template('login_user_form.html', form=form)



@app.route('/secret')
def secret():
    '''Presents a hidden page only for logged in users'''

    if 'user_id' not in session:
        flash('You must be logged in!', 'danger')
        return redirect('/login')
    else:
        return render_template('secret.html')



@app.route("/logout")
def logout():
    """Logs user out and redirect to homepage."""

    session.pop("user_id")

    return redirect("/")


@app.route("/users/<username>")
def show_user(username):
    """Redirect to user information page."""

    
    # always good to recheck authorization
    if 'user_id' not in session:
        flash("You must be logged in!", "danger")
        return redirect("/login")
    else: 
        user = User.query.get_or_404(username)

        return render_template("secret.html", user=user)