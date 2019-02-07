from flask import render_template,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

# Views
@main.route('/')
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

@main.route('/sources/<id>')
def articles(id):
    '''
    Shows Articles.
    '''
    story = get_articles(id)
    title = 'News Articles'

    return render_template('articles.html',title = title, story = story)