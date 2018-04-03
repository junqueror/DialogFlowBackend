from pprint import pprint

from flask import request
from flask_assistant import tell
from flask_restplus import Resource

from API.flaskWrapper import FlaskWrapper


class TestResource(Resource):

    @FlaskWrapper.Assistant.action('test')
    def test(self, testParam):

        print('In test resource')

        if testParam == 'test':
            msg = 'Has escrito "test"'
        elif testParam == 'prueba':
            msg = 'Has escrito "prueba"'
        else:
            msg = 'Has escrito  otra cosa'

        pprint(request)

        return tell(msg)
