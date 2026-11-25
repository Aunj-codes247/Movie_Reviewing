from flask import Blueprint, request, session
from model import save 


review = Blueprint( "review",__name__,template_folder='templates')


@review.route("/reviw", methods = ['POST'])
def moive_review():


    moive_review = request.form.get('rating')
    user_id = session.get('user_id')
    
