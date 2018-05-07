import getopt
import logging
import os
import sys
import traceback

from Application.app import App
from Application.settings import Settings
from DialogFlow.dialogFlowWrapper import DialogFlowWrapper
from Application.fileManager import FileManager

def getArguments(argv):
    debug = False
    try:
        opts, args = getopt.getopt(argv, 'ghf:d', ["debug"])
    except getopt.GetoptError as e:
        logging.error(traceback.format_exc())
        print('run.py -d')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--debug"):
            debug = True

    return debug


def configureLogger():
    if debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M')
    else:
        if not os.path.isdir('./log/'):
            os.mkdir('./log/')
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M', filename='./log/app.log', filemode='a')


# Start point of the process
if __name__ == "__main__":

    # Add project directory to the path environment variable
    parentdir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(parentdir)

    # Command arguments
    debug = getArguments(sys.argv[1:])

    # Logger configuration
    configureLogger()

    # Create the project application
    Application = App()

    # Built DialogFlow Agent schema
    os.environ['DEV_ACCESS_TOKEN'] = Settings.instance().DIALOGFLOW_DEV_TOKEN
    os.environ['CLIENT_ACCESS_TOKEN'] = Settings.instance().DIALOGFLOW_CLIENT_TOKEN

    templatesPath = os.path.join(parentdir, os.path.join('Application', 'templates'))
    yamlPath = os.path.join(templatesPath, 'entities.yaml')
    csvPath = os.path.join(templatesPath, 'entities.csv')
    print(yamlPath)
    print(csvPath)
    FileManager.SaveTemplatesCSV()
    DialogFlowWrapper.buildSchema()

    # Run the application
    Application.run(Settings.instance().FLASK_HOST, Settings.instance().FLASK_PORT)
    # logging.DEBUG(
    #     "Flask Application running on {0}:{1}".format(Settings.instance().FLASK_HOST, Settings.instance().FLASK_PORT))
