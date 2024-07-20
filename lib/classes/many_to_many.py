class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None

        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError ('title cannot be changed')
        if isinstance (new_title, str) and 5<=len(new_title)<=50:
            self._title = new_title
        else:
            raise ValueError (
                'Title must be between 5 and 50 characters inclusive'
            )
        
class Author:

    all = []
    def __init__(self, name):

        self._name = None
        
        self.name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError ('Name cannot be changed')
        
        if isinstance (new_name, str) and len(new_name)>0:
            self._name = new_name
        else:
            raise ValueError (
                'Name must be of type str and must be longer than 0 characters.'
            )

    def articles(self):
        return[article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
        pass

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        magazine.articles_list.append(new_article)
        self._articles.append(new_article)
        return new_article
        pass

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set(magazine.category for magazine in magazines ))

        pass

class Magazine:
    all = []

    def __init__(self, name, category):

        self._name = None
        self._category = None

        self.name = name
        self.category = category
        self.articles_list = []

        Magazine.all.append(self)
   
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2<=len(new_name)<=16:
            self._name = new_name
        else:
            raise ValueError(
                'Name must be string between 2 and 16 characters, inclusive'
            )

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category,str) and len(new_category)>0:
            self._category = new_category
        else:
            raise ValueError(
                'Category must be string longer than 0 characters.'
            )

    def articles(self):
        return[article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        return list(set(article.author for article in self.articles()))
        pass

    def article_titles(self):
        if not self.articles():
            return None
        return[article.title for article in self.articles()]
        pass

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] +=1
            else:
                author_counts[author] = 1
        contributing_authors = [author for author, count in author_counts.items() if count>2]

        if not contributing_authors:
            return None
        return contributing_authors



        pass