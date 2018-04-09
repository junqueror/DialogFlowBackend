import logging
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restplus import Api
from flask_restplus.namespace import Namespace
from Utils.singleton import Singleton


# Class to instantiate the api and its models
class FlaskWrapper:

    # Create api
    Api = Api(version='1.0', title='Flask API', description='API with basic structure')
    # Create a Flask WSGI application
    App = Flask(__name__)

    # API namespaces
    class Namespaces:
        dialogflow = Namespace(name='DialogFlow', description='Operations related with DialogFlow system')

    # Initialize the instance of App
    def __init__(self, config_class):

        # Set the Flask configuration
        FlaskWrapper.App.config.from_object(config_class)

        # Api configuration
        apiBlueprint = self._getApiBlueprint()
        FlaskWrapper.App.register_blueprint(apiBlueprint)

        # CORS
        CORS(FlaskWrapper.App)  # Initialize CORS on the application


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
        return FlaskWrapper.App.test_client()

