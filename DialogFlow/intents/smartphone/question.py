import random
from flask_assistant import context_manager, event

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def bestBattery(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getBestBattery, SmartPhone, quantity)
    # Create response message
    message = Message(['Listo! Estos son los móviles con batería de larga duración',
                       'Aquí los tienes',
                       'Estos son los que tienen batería de más capacidad'])
    message.addListOrCarrousel('Los {0} smartphones con más batería'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('bestBattery').lifespan = 2

    return message.response


@Agent.intentException
def cheapest(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getCheapests, SmartPhone, quantity)
    # Create response message
    message = Message(['Estos son los smartphones más baratos',
                       'Aquí tienes los móviles con el precio más bajo'])
    message.addListOrCarrousel('Los {0} smartphones más baratos'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('cheapest')

    return message.response


@Agent.intentException
def mostPowerful(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getMostPowerful, SmartPhone, quantity)
    # Create response message
    message = Message(['Listo! Estos son',
                       'Aquí los tienes',
                       'Los smartphones más potentes son los que tienen más cantidad de memoria RAM, y son los '
                       'siguientes'])
    message.addListOrCarrousel('Los {0} smartphones más potentes'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('mostPowerful').lifespan = 2
    return message.response


@Agent.intentException
def qualityPrice(request):
    # Get session object
    session = Session.getSession(request)

    # Create response message
    message = Message(Agent().getAgentSays(request))

    message.response.link_out(name='Huawei P20 Lite: el retorno del súperventas',
                              url='https://www.xataka.com/moviles/huawei-p20-lite-el-retorno-del-superventas')
    message.response.link_out(name='Huawei P20 Lite, la mejor gama media con doble cámara',
                              url='https://elandroidelibre.elespanol.com/2018/03/huawei-p20-lite.html')
    message.response.link_out(name='Huawei P20 Lite: calidad a precio asequible',
                              url='https://www.periodicoclm.es/articulo/comunicados/huawei-p20-lite-calidad-precio-asequible/20180516151504008288.html')  # Set contexts and lifespan
    message.response.suggest('Ver Huawei P20 Lite', 'Calidad-precio según los usuarios', 'Elegir gama')

    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('qualityPrice').lifespan = 2

    return message.response


@Agent.intentException
def qualityPriceUsers(request):
    # Get session object
    session = Session.getSession(request)

    # Get products from DB
    products, query = DbController().getAllFilterBy(SmartPhone, 'Samsung', ['company'], 'avgPrice')

    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.addCarrousel(products)

    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('qualityPriceUser').lifespan = 2

    return message.response
