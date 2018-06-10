import copy
from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message
from Application.settings import Settings
from Graphics.chartBuilder import ChartBuilder


@Agent.intentException
def showSmartphoneSelected(smartphoneBrand, smartphoneName):
    # Get products from DB
    smartphone = DbController().getOneByCompanyAndName(SmartPhone, smartphoneBrand, smartphoneName)
    # Create response message
    message = Message(['Aquí lo tienes'])
    message.addCard(smartphone)
    message.addSuggestions('Más detalles', 'Opiniones', 'Tiendas', 'Valoraciones')
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('product-selected').lifespan = 2
    context_manager.set('product-selected', 'productId', smartphone.id)
    return message.response


@Agent.intentException
def showSmartphonesDifferences(request, smartphoneBrand, smartphoneName):
    productSelectedId = int(context_manager.get_param('product-selected', 'productId'))

    # Get products from DB
    smartphone1 = DbController().getOne(SmartPhone, productSelectedId)
    smartphone2 = DbController().getOneByCompanyAndName(SmartPhone, smartphoneBrand, smartphoneName)

    if smartphone2:

        # Get differences as string
        differences1, differences2 = _getDifferences(smartphone1, smartphone2)

        # Generate chart
        chartCompleted = ChartBuilder().buildRadarChart(["{0} {1}".format(smartphone1.company, smartphone1.name),
                                                         "{0} {1}".format(smartphone2.company, smartphone2.name)],
                                                        ["Rendimiento", "Cámara", "Batería", "Pantalla", "Software"],
                                                        [smartphone1.rates, smartphone2.rates])

        # Create response message
        message = Message(Agent().getAgentSays(request))
        if chartCompleted:
            message = Message(Agent().getAgentSays(request))
            message.response = message.response.build_carousel()
            message.response.add_item(title='{0} {1}'.format(smartphone1.company, smartphone1.name),
                                      description=differences1,
                                      key='{0} {1}'.format(smartphone1.company, smartphone1.name))
            message.response.add_item(title='{0} {1}'.format(smartphone2.company, smartphone2.name),
                                      description=differences2,
                                      key='{0} {1}'.format(smartphone2.company, smartphone2.name))
            message.response.add_item(title='{0} {1} vs {2} {3}'.format(smartphone1.company, smartphone1.name,
                                                                        smartphone2.company, smartphone2.name),
                                      img_url=Settings().charts_endpoint,
                                      key = '{0} {1} vs {2} {3}'.format(smartphone1.company, smartphone1.name,
                                                                        smartphone2.company, smartphone2.name))

            # Set contexts and lifespans
            context_manager.add('smartphone')
            context_manager.add('product-selected')
    else:
        message = Message("Disculpa no he encontrado el {0} {1}".format(smartphoneBrand, smartphoneName))

    return message.response


@Agent.intentException
def showSmartphonesRates(request):
    productSelectedId = int(context_manager.get_param('product-selected', 'productId'))

    # Get products from DB
    smartphone = DbController().getOne(SmartPhone, productSelectedId)

    # Generate chart
    chartCompleted = ChartBuilder().buildRadarChart(["{0} {1}".format(smartphone.company, smartphone.name)],
                                   ["Rendimiento", "Cámara", "Batería", "Pantalla", "Software"],
                                   [smartphone.rates])

    message = Message(Agent().getAgentSays(request))
    if chartCompleted:
        # Create response message
        message.response.card(text='Valoración media: {0}'.format(smartphone.rate),
                              title="{0} {1}".format(smartphone.company, smartphone.name),
                              img_url=Settings().charts_endpoint)

        # Set contexts and lifespans
        context_manager.add('smartphone')
        context_manager.add('product-selected')

    return message.response


def _getDifferences(smartphone1, smartphone2):
    attributes1 = copy.deepcopy(smartphone1.__dict__)
    attributes1.pop('id')
    attributes1.pop('name')
    attributes1.pop('company')
    attributes1.pop('extras')
    attributes1.pop('officialURL')
    attributes1.pop('image')
    attributes1.pop('rangeId')
    differences = []
    for key, value in attributes1.items():
        if not key.lstrip().startswith('_') and not key.lstrip().startswith('rate') and getattr(smartphone1, key) and getattr(smartphone2, key):
            if getattr(smartphone1, key) != getattr(smartphone2, key):
                differences.append(key)
    text1 = ''.join(['{0}: {1}\n'.format(attr, getattr(smartphone1, attr)) for attr in differences])
    text2 = ''.join(['{0}: {1}\n'.format(attr, getattr(smartphone2, attr)) for attr in differences])
    return text1, text2
