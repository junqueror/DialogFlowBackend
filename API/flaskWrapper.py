from flask import Flask, Blueprint
from flask_cors import CORS
from Application.settings import Settings
from flask_restplus import Api
from flask_restplus.namespace import Namespace


# Class to instantiate the api and its models
class FlaskWrapper:
    # Create api
    Api = Api(version='1.0', title='Flask API', description='API with basic structure')

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
        api_blueprint = self.__GetApiBlueprint()
        self.app.register_blueprint(api_blueprint)

        # CORS
        CORS(self.app)  # Initialize CORS on the application


    # API blueprint definition
    def __GetApiBlueprint(self):

        # from API.Resources.articlesResource import ArticlesResource
        # from API.Resources.articleResource import ArticleResource
        # FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.articles, path='/articles')

        from API.Resources.DialogFlow.webHook import WebHookResource
        FlaskWrapper.Api.add_namespace(FlaskWrapper.Namespaces.dialogflow, path='/dialogflow')

        # Register blueprints and namespaces in the api
        bluePrint = Blueprint('API', __name__, url_prefix='/api')

        # Register namespaces in the api
        FlaskWrapper.Api.init_app(bluePrint)

        return bluePrint  # The API bluePrint

    # Return a Flask client for testing
    def getTestClient(self):
        return self.app.test_client()