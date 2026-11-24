from flask import Blueprint, render_template, request, session
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField , ValidationError
from wtforms.validators import DataRequired , EqualTo , length
from model import user, db


inside = Blueprint("inside", __name__, template_folder="templates", static_folder="static")
class UserMethod(FlaskForm):
    name = StringField('Username' , validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators= [DataRequired()])    
    submit = SubmitField('submit')
@inside.route("/login" , methods = ["POST", "GET"]) 
def login():
    form = UserMethod()

    if form.validate_on_submit():

        name = form.name.data.strip()
        email = form.email.data.strip()
        password = form.password.data.strip()
        
        
        usr = user(name = name, password=password, email = email)

        db.session.add(usr)
        db.session.commit()
    

    # else:
    #     message = "you have done something wrong"


    return render_template("login.html", form = form)


