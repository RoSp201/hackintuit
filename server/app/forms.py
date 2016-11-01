
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    #DataRequired is a validator, a function that can be attached to a field to
    #perform validation on data submitted by a user
    #the validator checks to make sure field submitted isn't empty
    openid = StringField('openid', validators=[DataRequired()])
    
    #this allows for a cookie to be generated for a user that wants to be remembered
    remember_me = BooleanField('remember_me', default=False)
