from DialogFlow.card import Card

class ResponseModel():

    def __init__(self, title, subtitle, sortText, longText, imgUrl, imgAlt, link, linkTitle, text):
        self.title = title
        self.subtitle = subtitle
        self.sortText = text
        self.longText = text
        self.imgUrl = imgUrl
        self.imgAlt = imgAlt
        self.link = link
        self.linkTitle = linkTitle

    def getBasicCard(self):
        return Card(title=self.title,
                    link=self.link,
                    linkTitle=self.linkTitle,
                    text=self.sortText,
                    )

    def getCompleteCard(self):
        return Card(title=self.title,
                    subtitle=self.subtitle,
                    link=self.link,
                    linkTitle=self.linkTitle,
                    img_url=self.imgUrl,
                    img_alt=self.imgAlt,
                    text=self.longText)

