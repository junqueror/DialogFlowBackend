from flask_assistant import Assistant, ask


class Response(ask):

    def __init__(self, speech, display_text=None):
        super(ask, self).__init__(speech, display_text)

    def buildIntegrationMessages(self):
        pass
