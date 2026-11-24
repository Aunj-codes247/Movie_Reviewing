from flask import Flask, render_template, request, session
from Lng.inside import inside
from Lng.alry import alry
from review.rendering import rendering
from model import db, user, save


app = Flask(__name__)
app.register_blueprint(inside , url_prefix = "")
app.register_blueprint(alry, url_prefix = "")
app.register_blueprint(rendering,url_prefix = "")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "Anujkumar123"

db.init_app(app)

# @app.route("/")
# def hello():
#     #  user_id = session.get('user_id')
#     #  message = f"wellcome {user_id}"

#      return render_template("index.html")
     

@app.route("/")
def home():

    first_user = user.query.all()
    user_id = session.get('user_id')
    
    
    return render_template("index.html", user_id = user_id)

# @app.route('/update/<int:id>', methods = ["POST"] )
# def update(id):
     


with app.app_context():
       db.create_all()

if __name__ == "__main__":
    app.run(debug=True)