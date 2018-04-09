from Application.flaskWrapper import FlaskWrapper
from flask_restplus import fields

class ApiModels:

    # Article Model
    ArticleModel = FlaskWrapper.Api.model('Article', {
        'id'
        'date': fields.DateTime(required=True, description='The creation date of the article'),
        'title': fields.String(required=True, description='The title of the article'),
        'text': fields.String(required=True, description='The article itself'),
        'author': fields.String(required=True, description='The author of the article')
    })

    # ===============================================================================
    # Request API Models
    # ===============================================================================

    # Article Model
    NewArticleModel = FlaskWrapper.Api.model(' New Article', {
        'text': fields.String(required=True, description='The article itself'),
        'title': fields.String(required=True, description='The title of the article'),
        'author': fields.String(required=True, description='The author of the article')
    })

    # ===============================================================================
    # Response API Models
    # ===============================================================================

    # Response Model for one Article
    ArticleResponseModel = FlaskWrapper.Api.model('Article Response Model', {
        'data': fields.Nested(ArticleModel, description='The article requested'),
        'succeed': fields.Boolean(description='Result of the action requested'),
        'errorMessage': fields.String(description='Message error when succeed is False'),
    })

    # Response Model for Article List
    ArticlesResponseModel = FlaskWrapper.Api.model('Articles Response Model', {
        'data': fields.List(fields.Nested(ArticleModel), description='List of articles'),
        'numResults': fields.Integer(description='Number of results expected in data'),
        'succeed': fields.Boolean(description='Result of the action requested'),
        'errorMessage': fields.String(description='Message error when succeed is False'),
    })
