class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,title,description,url):
        self.id =id
        self.name = name
        self.title = title
        self.description = description
        self.url=url
        
class Articles:
    '''
    Articles class that defines Articles Objects.
    '''

    def __init__(self,author,publishedAt,urlToImage,url):
        self.author = author
        self.publishedAt = publishedAt
        self.urlToImage = urlToImage
        self.url = url

