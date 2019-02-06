from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    inside = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')

    word = 'Welcome to News'
    return render_template('index.html', word=word, inside = inside ,business_sources = business_sources, technology_sources = technology_sources, entertainment_sources=entertainment_sources)

# @app.route('/articles/<id>')
# def articles(id):
#     '''
#     Shows Articles.
#     '''
#     story = get_articles(id)

#     title = 'News Articles'

#     return render_template('articles.html',title = title, story = story)