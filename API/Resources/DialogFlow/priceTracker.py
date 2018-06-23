from flask import request, send_file
from flask_restplus import Resource
from Application.flaskWrapper import FlaskWrapper
from Application.settings import Settings


@FlaskWrapper.Namespaces.dialogflow.route('/priceTracker')
class PriceTrackerResource(Resource):
    # GET
    @FlaskWrapper.Api.doc('Get for price tracker')
    @FlaskWrapper.Api.response(200, 'Success')
    def get(self):
        return send_file(Settings().priceTracker_filePath, mimetype='image/png')
