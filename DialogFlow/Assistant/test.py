from flask_assistant import ask
from DialogFlow.dialogflowWrapper import DialogFlowWrapper


class TestResource():

    @DialogFlowWrapper.Assistant.action('test')
    def test(testParam):
        print('In test resource')

        if testParam == 'test':
            msg = 'Has escrito "test"'
        elif testParam == 'prueba':
            msg = 'Has escrito "prueba"'
        else:
            msg = 'Has escrito otra cosa'

        return ask(msg)