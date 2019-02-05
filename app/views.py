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
    world_sources = get_sources('world')
    top_sources = get_sources('top')


    word = 'Welcome to News'
    return render_template('index.html', word=word, inside=inside, world_sources = world_sources, top_sources=top_sources )

# @app.route('/articles/<id>')
# def articles(id)
#     '''
#     Shows Articles.
#     '''
#     story = get_articles(id)

#     title = 'In the Top Story'

#     return render_template('articles.html',title = title, story = story)