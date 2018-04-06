from flask_assistant import ask
from flask_restplus import Resource

from API.flaskWrapper import FlaskWrapper


class TestResource(Resource):

    @FlaskWrapper.Assistant.action('test')
    def test(testParam):
        print('In test resource')

        if testParam == 'test':
            msg = 'Has escrito "test"'
        elif testParam == 'prueba':
            msg = 'Has escrito "prueba"'
        else:
            msg = 'Has escrito otra cosa'

        return ask(msg)