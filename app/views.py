from flask import render_template
from app import app
from .request import get_sources,get_articles

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
    health_sources = get_sources('health')

    word = 'Welcome to News'
    return render_template('index.html', word=word, inside = inside ,business = business_sources, technology = technology_sources, entertainment=entertainment_sources, health=health_sources)

@app.route('/sources/<id>')
def articles(id):
    '''
    Shows Articles.
    '''
    story = get_articles(id)
    title = 'News Articles'

    return render_template('articles.html',title = title, story = story)