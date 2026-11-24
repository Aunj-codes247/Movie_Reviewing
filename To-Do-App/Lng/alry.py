from flask_sqlalchemy import SQLAlchemy
from flask import render_template, Blueprint, request,redirect,url_for,session
from model import user

alry = Blueprint("alry",__name__, template_folder="templates")


@alry.route("/signin", methods = ["POST", "GET"])
def signin():
    message = None

    if request.method == "POST":


      name = request.form.get("name")
      inital_password = request.form.get("password")

      print("anythnig")
      found_user = user.query.filter_by(name=name).first()
        

      if found_user and found_user.verify_password(inital_password):
            session['user_id'] = found_user.id
            
            return redirect(url_for("home"))

           

    else:
          message = "you are a fool"

      

    return render_template("signin.html", message = message)






