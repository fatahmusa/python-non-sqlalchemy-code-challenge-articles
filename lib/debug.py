#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()



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
        return self.articles_list
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass