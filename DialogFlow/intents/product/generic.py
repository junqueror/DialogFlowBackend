from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.assistantWrapper import AssistantWrapper
from DialogFlow.session import Session
from DialogFlow.message import Message


@AssistantWrapper.intentException
def askCategory():
    message = Message(['¿Qué estás buscando?',
                      '¿Qué te gustaría comprar?',
                      '¿Qué tipo de producto te interesa?',
                      'Dime una categoría de producto para empezar'])
    return message.response