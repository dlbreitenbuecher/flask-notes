"""Forms to register users."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
# from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email


class AddUserForm(FlaskForm):
    """Add/Register user form."""

    username = StringField("Username", validators=[InputRequired(),
                                                        Length(min=1, max=20)])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email Address", validators=[InputRequired()])
    # Email() is an issue
    first_name = StringField("First Name", validators=[InputRequired(), 
                                                        Length(min=1, max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), 
                                                        Length(min=1, max=30)])