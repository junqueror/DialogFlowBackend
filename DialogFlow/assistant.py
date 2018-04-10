import logging
import random
from flask_assistant import Assistant, ask
from Application.flaskWrapper import FlaskWrapper
from DataBase.dbController import DbController
from DataBase.DataModels import *
from flask_assistant import context_manager

# Create assistant
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
Assistant = Assistant(app=FlaskWrapper.App, route='/assistant')


# Intents

@Assistant.action('sp.category>range')
def askRange():
    basicResponses = ['¿Qué categoría de móvil estás buscando?',
                      '¿Qué rango de SmartPhones te interesa?',
                      'Elije una de las siguientes gamas para poder empezar',
                      'Lo primero es elegir la gama de SmartPhones que buscamos. Ten encuenta que de esta decisión depende bastante el precio, por lo que te recomiendo que elijas de acuerdo a tus necesidades reales. No queremos gastar dinero en algo que no necesitamos!']
    ranges = DbController.instance().getAll(Range)
    response = ask(random.choice(basicResponses)).build_carousel()

    for range in ranges:
        response.add_item(title=range.name, key=range.name, description=range.description)

    context_manager.add('sp.range')

    return response


@Assistant.context('sp.range')
@Assistant.action('sp.range>screen')
def askScreen(smartphoneRange):
    basicResponses = [
        'Vamos a empezar por las dimensiones del SmartPhone, que dependen principalmente del tamaño de pantalla.',
        'Las dimensiones del SmartPhone determinan su tamaño. ¿Qué tamaño de pantalla estás buscando?']
    range = DbController.instance().getOneByName(Range, smartphoneRange)

    response = ask(random.choice(basicResponses)).build_carousel()
    for screen in range.screens:
        response.add_item(title=screen.name, key=screen.name, description=screen.description)

    context_manager.add('sp.screen')

    return response


@Assistant.action('smartphone')
def showSmartphoneCard(smartphoneBrand, smartphoneName):
    smartphone = DbController.instance().getOneByCompanyAndName(SmartPhone, smartphoneBrand, smartphoneName)

    response = ask('Aquí lo tienes:')
    response.card(title="{0} {1}".format(smartphone.company, smartphone.name),
                  link=smartphone.officialURL,
                  linkTitle='Web oficial',
                  text="Precio medio: {0!s}€".format(smartphone.avgPrice))
    return response


# Prompts

@Assistant.prompt_for('smartphoneName', intent_name='smartphone')
def promptSmartphoneName(smartphoneName):
    response = "¿Podrías decirme el nombre del teléfono que estás buscando?"
    return ask(response)


@Assistant.prompt_for('smartphoneBrand', intent_name='smartphone')
def promptSmartphoneBrand(smartphoneBrand):
    response = "¿Cuál la marca del smartphone que estás buscando?"
    return ask(response)


@Assistant.prompt_for('smartphoneRange', intent_name='sp.range>screen')
def promptSmartphoneRange(smartphoneRange):
    response = "¿Podrias decirme la gama de SmartPhone en la que estás interesado?"
    return ask(response)
