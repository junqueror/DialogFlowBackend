import sys
from api_ai.cli import schema

class DialogFlowWrapper():

    @staticmethod
    def buildSchema():

        sys.argv.insert(1,'DialogFlow/assistant.py')
        schema()