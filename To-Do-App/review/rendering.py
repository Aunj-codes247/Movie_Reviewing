import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, session
from model import save, db

rendering = Blueprint("rendering", __name__ , template_folder="templates", static_folder="static")

load_dotenv()


@rendering.route("/movies", methods=['POST', 'GET'])
def movies():

    if request.method == 'POST':

        movie_review = request.form.get('rating')
        user_id = session.get('user_id')
        movie_id = request.form.get('movie_id')
        if movie_review and user_id and movie_id:
            lst = save(Rating= movie_review, user_id = user_id , movie_id = movie_id )
            db.session.add(lst)
            db.session.commit()

    movie_title = request.args.get('q','Toy Story')
    API_KEY = os.getenv("API_KEY")

    response = requests.get(f"https://www.omdbapi.com/?apikey={API_KEY}&s={movie_title}")

    data = response.json()
    movie_list = data.get("Search", [])

    return render_template("rendering.html", posts = movie_list)



    

# @rendering.route("/movies_reviews", methods = ['POST', 'GET'])
# def review_movie():
   


        # moive_review = request.form.get('rating')
        # user_id = session.get('user_id')
        # moive_id = request.form.get('moive_id')
    
        # lst = save(Rating=moive_review, user_id = user_id, movie_id = moive_id)
    
        # db.session.add(lst)
        # db.session.commit()
    
#         return render_template("rendering.html")






    
