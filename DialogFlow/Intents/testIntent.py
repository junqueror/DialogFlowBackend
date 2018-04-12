from flask_assistant import ask
from DialogFlow.assistant import Assistant


class TestIntent():

    @Assistant.action('testIntent')
    def test(self):
        response = ask('IN TEST INTENT')

        return response
