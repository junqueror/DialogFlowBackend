from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels import *
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def getCategoryAskRange(request):

    ranges = DbController().getAll(Range)
    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.response = message.response.build_carousel()
    for range in ranges:
        message.response.add_item(title=range.name, key=range.name, description=range.description)

    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('product.category>sp.range')

    return message.response


@Agent.intentException
def getRangeAskScreen(request, smartphoneRange):
    # Get from DB
    range = DbController().getOneByName(Range, smartphoneRange)
    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.response = message.response.build_carousel()
    for screen in range.screens:
        message.response.add_item(title=screen.name, key=screen.name, description=screen.description)

    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('sp.range>screen')

    return message.response
