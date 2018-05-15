import sys
import logging
import random
from api_ai.cli import schema
from Application.fileManager import FileManager
from DialogFlow.message import Message


class AssistantWrapper():
    @staticmethod
    def buildSchema():

        sys.argv.insert(1, 'DialogFlow/assistant.py')
        schema()

    @staticmethod
    def intentException(func):
        def decorator(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logging.error('Error on intent <{0}>: {1}'.format(func, e))
                message = Message([''])
                message.response.card(text=random.choice(['Disculpa, he petado y no puedo responder a tu petición',
                                                          'Upsss... He roto internamente y no podré responderte',
                                                          'Algo ha ido mal']),
                                      img_url=random.choice([
                                                                "https://media1.tenor.com/images/94fd4b239642ee7875dafa52b1daf92f/tenor.gif?itemid=9711586",
                                                                "https://media1.tenor.com/images/e45c8474011c72c4ee70b4b9909903d3/tenor.gif?itemid=5612475",
                                                                "https://media.tenor.com/images/8474b0f567704b752354d6e5a589784b/tenor.gif",
                                                                "https://media1.tenor.com/images/fc000ba0b39c56c1480f00d9a5793b1c/tenor.gif?itemid=4841810"]))
                return message.response

        return decorator