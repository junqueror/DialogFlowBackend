import logging
from flask import Flask, Blueprint
from flask_cors import CORS
from Application.settings import Settings
from flask_restplus import Api
from flask_assistant import Assistant
from flask_restplus.namespace import Namespace


# Class to instantiate the api and its models
class FlaskWrapper:
    # Create api
    Api = Api(version='1.0', title='Flask API', description='API with basic structure')
    Assistant = Assistant(route=None)

    # Create Assisntat

    # API namespaces
    class Namespaces:
        # articles = Namespace(name='Articles', description='Operations related to articles')
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
        assistantBlueprint = self._GetAssistantBlueprint()
        self.app.register_blueprint(assistantBlueprint)

        # CORS
        CORS(self.app)  # Initialize CORS on the application


    # API blueprint definition
    def _GetApiBlueprint(self):

        # from API.Resources.articlesResource import ArticlesResource
        # from API.Resources.articleResource import ArticleResource
        # FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.articles, path='/articles')

        from API.Resources.DialogFlow.webHook import WebHookResource
        FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.dialogflow, path='/dialogflow')

        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('API', __name__, url_prefix='/api')

        # Register namespaces in the api
        FlaskWrapper.Api.init_app(self.app)

        return bluePrint  # The API bluePrint

    # Assistant blueprint definition
    def _GetAssistantBlueprint(self):
        logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('Assistant', __name__, url_prefix='/assistant')

        # Register blueprint in the assistant
        FlaskWrapper.Assistant.init_blueprint(bluePrint)

        return bluePrint  # The API bluePrint


    # Return a Flask client for testing
    def getTestClient(self):
        return self.app.test_client()