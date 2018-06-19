from flask_assistant import context_manager, event

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def questionOrHelp(request, productCategory):
    if productCategory == 'Smartphone':
        message = Message(Agent().getAgentSays(request))
    else:
        # Create response message
        message = Message(['Lo siento, pero ahora mismo solo puedo ayudarte con la categoría de SmartPhones.'])

    # Set contexts and lifespans
    context_manager.add('help')

    return message.response
