import logging
import traceback
from flask import request
from flask_restplus import Resource
from Application.flaskWrapper import FlaskWrapper
from API.apiModels import ApiModels
from DataBase.dbController import DbController
from DataBase.DataModels.article import Article


@FlaskWrapper.Namespaces.articles.route('/')
class ArticlesResource(Resource):

    # GET
    @FlaskWrapper.Api.doc('GET the list of the articles')
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.marshal_with(ApiModels.ArticlesResponseModel)
    def get(self):

        # Initialize response
        articles = []
        numResults = 0
        succeed = False
        errorMessage = ''

        try:
            # Get articles from database
            articles, numResults = DbController.instance().getAll(Article)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error(
                "There was an issue retrieving the list of articles: ({0}) : {1}".format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue retrieving the list of articles'

        return dict(data=articles, numResults=numResults, succeed=succeed, errorMessage=errorMessage)

    # POST
    @FlaskWrapper.Api.doc('POST for creating a new article')
    @FlaskWrapper.Api.expect(ApiModels.NewArticleModel)
    @FlaskWrapper.Api.marshal_with(ApiModels.ArticleResponseModel)
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.response(400, 'Parameter validation Error')
    def post(self):

        # Get the parameters included in the request
        title = request.get_json().get('title').strip()
        text = request.get_json().get('text').strip()
        author = request.get_json().get('author').strip()

        # Initialize response
        newArticle = None
        succeed = False
        errorMessage = ''

        try:
            # Create article in the database
            newArticle = Article(title=title,
                                 text=text,
                                 author=author)
            DbController.instance().add(newArticle)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue crating a new article: ({0}) : {1}"
                          .format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue creating a new the article'

        return dict(data=newArticle, succeed=succeed, errorMessage=errorMessage)
