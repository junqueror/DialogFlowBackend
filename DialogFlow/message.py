import random
from flask_assistant import ask


class Message():

    def __init__(self, messages):
        self.response = ask(random.choice(messages))

    def addCard(self, element):

        self.response.card(title=element.title,
                           link=element.link,
                           linkTitle=element.linkTitle,
                           text=element.text,
                           img_url=element.imgUrl)

    def addCarrousel(self, elements):
        self.response = self.response.build_carousel()
        for element in elements:
            self.response.add_item(title=element.title,
                                   key=element.key,
                                   description=element.description,
                                   img_url=element.imgUrl,
                                   synonyms=element.synonyms)

    def addList(self, title, elements):
        self.response = self.response.build_list(title)
        for element in elements:
            self.response.add_item(title=element.title,
                                   key=element.key,
                                   description=element.description,
                                   img_url=element.imgUrl,
                                   synonyms=element.synonyms)

    def addSuggestions(self, *args):
        self.response.suggest(*args)
