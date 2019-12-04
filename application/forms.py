from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import Account_details


class AccountUpdateForm(FlaskForm):
    new_login = StringField("new_login",
        validators=[
                DataRequired()
            ]
        )

    submit = SubmitField("Change")

    def validate_login(self, login):
        if login.data != current_user.login:
            user = Account_details.query.filter_by(login = login.data).first()

            if user:
                raise ValidationError("Login already in database.")



class LoginForm(FlaskForm):
    login = StringField("login",
        validators=[
                DataRequired()
            ]
        )

    password = PasswordField("password",
        validators=[
                DataRequired()
            ]
        )

    remember = BooleanField("Remember me")
    submit = SubmitField("Login")



class RegistrationForm(FlaskForm):
    login = StringField("login",
        validators=[
                DataRequired()
            ]
        )

    password = PasswordField("password",
        validators=[
                DataRequired()
            ]
        )

    confirm_password = PasswordField("Confirm Password",
        validators=[
                DataRequired(),
                EqualTo("password")
            ]
        )

    submit = SubmitField("Sign up")
    
    def validate_login(self, login):
        user = Account_details.query.filter_by(login = login.data).first()

        if user:
            raise ValidationError("Login already in database.")


