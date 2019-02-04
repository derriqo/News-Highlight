class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,title,description):
        self.id =id
        self.name = name
        self.title = title
        self.description = description
        
class Articles:
    '''
    Articles class that defines Articles Objects.
    '''

    def __init__(self,author,publishedAt):
        self.author = author
        self.publishedAt = publishedAt

