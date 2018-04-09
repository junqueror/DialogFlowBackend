from DialogFlow.card import Card

class RichMessage():

    title = None
    officialURL = None
    extras = None

    def getCard(self):
        return Card(title=self.title, link=self.officialURL, linkTitle='Web oficial', text=self.extras)


