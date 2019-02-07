import urllib.request,json
from .models import Source,Articles

# Source = source.Source
# Articles = source.Articles

api_key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config["SOURCE_API_URL"]
    articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category,api_key)


    with urllib.request.urlopen(get_sources_url) as url:
            get_sources_data = url.read()
            get_sources_response = json.loads(get_sources_data)
            
            source_results = None

            if get_sources_response["sources"]:
                source_results_list = get_sources_response["sources"]
                source_results = process_results(source_results_list)
        
    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and transforms them to a list of objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        title = source_item.get('title')
        description = source_item.get('description')
        url=source_item.get('url')

        source_object = Source(id,name,title,description,url)
        source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

       
        articles_results = None

        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = receive_results(articles_results_list)

    return  articles_results
        

def receive_results(articles_list):
    '''
    Function that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain source details
    Returns :
        articles_results: A list of articles objects
    '''


    articles_results = []
    for articles_item in articles_list:
        
        author = articles_item.get('author')
        publishedAt = articles_item.get('publishedAt')
        urlToImage = articles_item.get('urlToImage')
        url = articles_item.get('url')
        description = articles_item.get('description')
        
        articles_object = Articles(author,publishedAt,urlToImage,url,description)
        articles_results.append(articles_object)
    return articles_results