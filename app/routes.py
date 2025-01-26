from app import app
from .generator import make_character

@app.route('/')
def index():
    """Home page of the site, displaying the recommender form"""
    return make_character()
