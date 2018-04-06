import logging

from flask import Flask, Blueprint
from flask_assistant import Assistant
from flask_cors import CORS
from flask_restplus import Api
from flask_restplus.namespace import Namespace


# Class to instantiate the api and its models
class FlaskWrapper:
    # Create api
    Api = Api(version='1.0', title='Flask API', description='API with basic structure')

    # Create assistant
    Assistant = Assistant(route='/assistant')

    # API namespaces
    class Namespaces:
        dialogflow = Namespace(name='DialogFlow', description='Operations related with DialogFlow system')

    # Initialize the instance of App
    def __init__(self, config_class):
        # Create a Flask WSGI application
        self.app = Flask(__name__)
        # Set the Flask configuration
        self.app.config.from_object(config_class)

        # DialogFlow Assistant configuration
        self._initAssistant()

        # Api configuration
        apiBlueprint = self._getApiBlueprint()
        self.app.register_blueprint(apiBlueprint)

        # CORS
        CORS(self.app)  # Initialize CORS on the application

    def _initAssistant(self):
        logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
        FlaskWrapper.Assistant.init_app(self.app)

    # API blueprint definition
    def _getApiBlueprint(self):

        FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.dialogflow, path='/dialogflow')

        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('Api', __name__, url_prefix='/api')

        # Register namespaces in the api
        FlaskWrapper.Api.init_app(bluePrint)

        return bluePrint  # The API bluePrint

    # Return a Flask client for testing
    def getTestClient(self):
        return self.app.test_client()

