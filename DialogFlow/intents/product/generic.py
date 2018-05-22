from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def askCategory(request):
    phrases = Agent().getAgentSays(request)
    message = Message(phrases)
    return message.response