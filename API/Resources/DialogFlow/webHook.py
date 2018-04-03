import logging
import traceback
from pprint import pprint
from flask import request
from flask_restplus import Resource
from API.flaskWrapper import FlaskWrapper
from API.apiModels import ApiModels
from DataBase.dbController import DbController


@FlaskWrapper.Namespaces.dialogflow.route('/webhook')
class WebHookResource(Resource):

    # POST
    @FlaskWrapper.Api.doc('POST for DialogFlow requests')
    # @FlaskWrapper.Api.expect(ApiModels.NewArticleModel)
    # @FlaskWrapper.Api.marshal_with(ApiModels.ArticleResponseModel)
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.response(400, 'Parameter validation Error')
    def post(self):

        # Get the parameters included in the request
        requestData = request.json

        # Initialize response
        newArticle = None
        succeed = False
        errorMessage = ''

        try:
            pprint(requestData)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue on DialogFlow WebHook: ({0}) : {1}"
                          .format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue on DialogFlow WebHook'

        return succeed
