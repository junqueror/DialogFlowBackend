from flask import Flask, Blueprint
from flask_assistant import Assistant
from flask_assistant import tell
from flask_cors import CORS
from flask_restplus import Api
from flask_restplus.namespace import Namespace


# Class to instantiate the api and its models
class FlaskWrapper:
    # Create api
    Api = Api(version='1.0', title='Flask API', description='API with basic structure')

    # Create assistant
    Assistant = Assistant(route=None)

    # API namespaces
    class Namespaces:
        dialogflow = Namespace(name='DialogFlow', description='Operations related with DialogFlow system')

    # Initialize the instance of App
    def __init__(self, config_class):
        # Create a Flask WSGI application
        self.app = Flask(__name__)
        # Set the Flask configuration
        self.app.config.from_object(config_class)

        # Api configuration
        apiBlueprint = self._GetApiBlueprint()
        self.app.register_blueprint(apiBlueprint)

        # DialogFlow Assistant configuration
        assistantBlueprint = self._GetDialogFlowBlueprint()
        self.app.register_blueprint(assistantBlueprint)

        # CORS
        CORS(self.app)  # Initialize CORS on the application


    # API blueprint definition
    def _GetApiBlueprint(self):

        FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.dialogflow, path='/dialogflow')

        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('Api', __name__, url_prefix='/api')

        # Register namespaces in the api
        FlaskWrapper.Api.init_app(bluePrint)

        return bluePrint  # The API bluePrint

    # Assistant blueprint definition
    def _GetDialogFlowBlueprint(self):
        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('Dialogflow', __name__, url_prefix='/dialogflow/assistant')

        # Register blueprint in the assistant
        FlaskWrapper.Assistant.init_blueprint(bluePrint)

        return bluePrint  # The API bluePrint

    # Return a Flask client for testing
    def getTestClient(self):
        return self.app.test_client()


@FlaskWrapper.Assistant.action('test')
def test():
    print('In test resource')
    #
    # if testParam == 'test':
    #     msg = 'Escribiste "test"'
    # elif testParam == 'prueba':
    #     msg = 'Escribiste "prueba"'
    # else:
    #     msg = 'Escribiste otra cosa'

    return tell('test response')
