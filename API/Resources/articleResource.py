import logging
import traceback
from flask import request
from flask_restplus import Resource
from API.flaskWrapper import FlaskWrapper
from API.apiModels import ApiModels
from DataBase.dbController import DbController
from DataBase.DataModels.article import Article


@FlaskWrapper.Namespaces.articles.route('/<int:articleID>')
class ArticleResource(Resource):

    # GET
    @FlaskWrapper.Api.doc('GET the list of the articles')
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.marshal_with(ApiModels.ArticleResponseModel)
    def get(self, articleID):

        # Initialize response
        article = None
        succeed = False
        errorMessage = ''

        try:
            # Get article from database
            article = DbController.instance().getOne(Article, articleID)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue retrieving the article: ({0}) : {1}"
                          .format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue retrieving the article'

        return dict(data=article, succeed=succeed, errorMessage=errorMessage)

    # PUT
    @FlaskWrapper.Api.doc('Put for modifying the article')
    @FlaskWrapper.Api.expect(ApiModels.NewArticleModel)
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.response(400, 'Parameter validation Error')
    @FlaskWrapper.Api.marshal_with(ApiModels.ArticleResponseModel)
    def put(self, articleID):

        # Get the parameters included in the request
        title = request.get_json().get('title').strip()
        text = request.get_json().get('text').strip()
        author = request.get_json().get('author').strip()

        # Initialize response
        article = None
        succeed = False
        errorMessage = ''

        try:
            # Update the article on DataBase
            article = DbController.instance().getOne(Article, articleID)
            article.title = title
            article.text = text
            article.author = author
            DbController.instance().commitDB()

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue modifying the article: ({0}) : {1}"
                          .format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue modifying the article'

        return dict(data=article, succeed=succeed, errorMessage=errorMessage)

    # DELETE
    @FlaskWrapper.Api.doc('DELETE for deleting an article')
    @FlaskWrapper.Api.marshal_with(ApiModels.ArticleResponseModel)
    @FlaskWrapper.Api.response(200, 'Success')
    def delete(self, articleID):

        # Initialize response
        succeed = False
        errorMessage = ''

        try:
            # Delete article from database
            DbController.instance().delete(Article, articleID)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue deleting the article: ({0}) : {1}".format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue deleting the article'

        return dict(succeed=succeed, errorMessage=errorMessage)
