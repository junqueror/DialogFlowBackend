from pprint import pprint
from flask import request
from flask_restplus import Resource
from flask_assistant import tell
from API.flaskWrapper import FlaskWrapper


class TestResource(Resource):

    @FlaskWrapper.Assistant.action('test')
    def test(self, testParam):

        if testParam == 'test':
            msg = 'Escribiste "test"'
        elif testParam == 'prueba':
            msg = 'Escribiste "prueba"'
        else:
            msg = 'Escribiste otra cosa'

        pprint(request)

        return tell(msg)
