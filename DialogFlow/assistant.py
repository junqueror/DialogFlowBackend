import logging
from flask_assistant import Assistant, ask
from Application.flaskWrapper import FlaskWrapper
from DataBase.dbController import DbController
from DataBase.DataModels import *

# Create assistant
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
Assistant = Assistant(app=FlaskWrapper.App, route='/assistant')


# Intents

@Assistant.action('sp.category>range')
def askRange():
    response = ask(
        'Lo primero es elegir la gama de smartphone que buscamos. Ten encuenta que de esta decisión depende bastante el precio, por lo que te recomiendo que elijas de acuerdo a tus necesidades reales. No queremos gastar dinero en algo que no necesitamos!').build_carousel()
    response.add_item(title='Gama baja', key='Gama baja',
                      description='Estos smartphones se centran en tener un precio muy reducido, a costa de ofrecer solo funcionalidades básicas. Si buscas un móvil solo para hablar por teléfono, chatear, navegación web, con una pantalla y dimensiones contenidas y sencillez de uso, ésta es tu opción.')
    response.add_item(title='Gama media', key='Gama media',
                      description='Smartphones con un buen rendimiento en la mayoría de las funciones habituales. Mejoran en cámara, pantalla y fluidez a los terminales de gama baja. Si buscas calidad-precio en términos generales es la mejor opción, pero si quieres utilizar muchas aplicacciones simultáneamente y jugar de vez en cuando tal vez debas elegir una gama superior.')
    response.add_item(title='Gama alta', key='Gama alta',
                      description='Smartphones con un buen rendimiento en todos los aspectos. Cuentan con mejores procesadores y mayor cantidad de memoria, lo que les permite utilizar varias aplicaciones simultáneamente y ejecutar juegos con buena fluidez. Suelen contar con cámara de altas prestaciones y una pantalla de mejor calidad y resolución. Por contra, elevan su precio respecto a las gamas previas.')
    response.add_item(title='Gama premium', key='Gama premium',
                      description='Los mejores smartphones del mercado. Los buques insignia de cada una de las marcas. Cuentan con las últimas tecnologías y destacan en prácticamente todos los aspectos. La mejor opción si haces un uso intensivo del móvil, juegas, utilizas todas las funcionalidades que puede ofrecerte, siempre que quieras y puedas pagar un precio más elevado.')

    return response

# @Assistant.action(intent_name='test')
# def test(testParam=''):
#     print('In test resource')
#
#     if testParam == 'test':
#         msg = 'Has escrito "test"'
#     elif testParam == 'prueba':
#         msg = 'Has escrito "prueba"'
#     else:
#         msg = 'Has escrito otra cosa'
#
#     return ask(msg)


@Assistant.action('smartphone')
def showSmartphoneCard(smartphoneBrand, smartphoneName):
    smartphone = DbController.instance().getOneByBrandAndName(SmartPhone, smartphoneBrand, smartphoneName)

    response = ask('Aquí lo tienes:').build_carousel()
    response.card(smartphone.getCard())

    return response


@Assistant.prompt_for('smartphoneName', intent_name='smartphone')
def prompt_smartphoneName(smartphoneName):
    response = "¿Podrías decirme el nombre del teléfono que estás buscando?"
    return ask(response)


@Assistant.prompt_for('smartphoneBrand', intent_name='smartphone')
def prompt_smartphoneRange(smartphoneBrand):
    response = "¿Podrías decirme la marca del smartphone que estás buscando?"
    return ask(response)
