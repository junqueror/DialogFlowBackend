from flask import request, send_file
from flask_restplus import Resource
from Application.flaskWrapper import FlaskWrapper
from Application.settings import Settings


@FlaskWrapper.Namespaces.dialogflow.route('/chart')
class ChartResource(Resource):
    # GET
    @FlaskWrapper.Api.doc('Get for radio charts')
    @FlaskWrapper.Api.response(200, 'Success')
    def get(self):
        return send_file(Settings().charts_filePath, mimetype='image/gif')
