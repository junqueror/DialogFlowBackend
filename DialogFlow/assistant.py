import logging
import random
from flask_assistant import Assistant, ask, context_manager
from Application.flaskWrapper import FlaskWrapper
from DialogFlow.intents.smartphone import filterPath, question, selected, search
from DialogFlow.intents.ecommerce import generic as genericEcommerce
from DialogFlow.intents.product import generic as genericProduct
from DialogFlow.agent import Agent

# ----------------------------------------------- ASSISTANT --------------------------------------------
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
Assistant = Assistant(app=FlaskWrapper.App, route='/assistant')


# ----------------------------------------------- -ROUTING ---------------------------------------------

@Assistant.action('push.notification')
def pushNotification():
    print("PUSH")
    response = ask("Ha llegado la notificación push?")
    return response


@Assistant.action('buy>product.category')
def askProductCategory():
    return genericProduct.askCategory(Assistant.request)


@Assistant.action('product.category>sp.range')
def askRange(productCategory):
    return filterPath.getCategoryAskRange(Assistant.request, productCategory)


@Assistant.context('smartphone')
@Assistant.action('sp.range>screen')
def askScreen(smartphoneRange):
    return filterPath.getRangeAskScreen(smartphoneRange)


@Assistant.context('smartphone')
@Assistant.action('sp.screen>RAM')
def askRAM(smartphoneScreen):
    print("IN sp.screen>RAM")
    smartphoneRange = context_manager.get('smartphone', 'smartphoneRange')
    print(smartphoneScreen)
    print(smartphoneRange)

    return ask('In sp.screen>RAM')

@Assistant.action('sp.selected')
def showSmartphoneSelected(smartphoneName, smartphoneBrand=None):
    return selected.showSmartphoneCard(smartphoneBrand, smartphoneName)


@Assistant.context('smartphone')
@Assistant.context('product-selected')
@Assistant.action('sp.selected.ecommerce')
def showSmartphoneSelectedEcommerces():
    return genericEcommerce.getSmartphoneShowEcommerces()


@Assistant.context('product-selected')
@Assistant.action('sp.selected.differences')
def showSmartphonesDifferences(smartphoneName, smartphoneBrand):
    return selected.showDifferencesCarousel(Assistant.request, smartphoneBrand, smartphoneName)


@Assistant.action('sp.question.mostPowerful')
def showMostPowerfulSmartphones(quantity=5):
    return question.mostPowerful(Assistant.request, quantity)


@Assistant.action('sp.question.cheapest')
def showCheapestSmartphones(quantity=5):
    return question.cheapest(Assistant.request, quantity)


@Assistant.action('sp.question.bestBattery')
def showBestBatterySmartphones(quantity=5):
    return question.bestBattery(Assistant.request, quantity)

@Assistant.action('sp.question.qualityPrice')
def questionQualityPrice():
    return question.qualityPrice(Assistant.request)

@Assistant.action('sp.question.qualityPriceUsers')
def questionQualityPriceUsers():
    return question.qualityPriceUsers(Assistant.request)


@Assistant.action('sp.search.generic')
def showSmartphonesSearched(quantity=5):
    return search.generic(Assistant.request, quantity)


# ----------------------------------------------- PROMPTS --------------------------------------------

@Assistant.prompt_for('smartphoneName', intent_name='smartphone')
def promptSmartphoneName(smartphoneName):
    response = "¿Podrías decirme el nombre del teléfono que estás buscando?"
    return ask(response)


# @Assistant.prompt_for('smartphoneBrand', intent_name='smartphone')
# def promptSmartphoneBrand(smartphoneBrand):
#     response = "¿Cuál la marca del smartphone que estás buscando?"
#     return ask(response)
#
#
# @Assistant.prompt_for('smartphoneRange', intent_name='sp.range>screen')
# def promptSmartphoneRange(smartphoneRange):
#     response = "¿Podrías decirme la gama de SmartPhone en la que estás interesado?"
#     return ask(response)

@Assistant.prompt_for('smartphoneBrand', intent_name='sp.selected.differences')
def promptSmartphoneBrand(smartphoneBrand):
    response = "¿Cuál la marca del SmartPhone con el que quieres comparar?"
    return ask(response)


@Assistant.prompt_for('smartphoneName', intent_name='sp.selected.differences')
def promptSmartphoneName(smartphoneName):
    response = "¿Podrías decirme el nombre del SmartPhone que quieres comparar?"
    return ask(response)
