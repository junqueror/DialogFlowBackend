# import os
# import sys
# import getopt
# import logging
# import traceback
# from Application.settings import Settings
# from Application.app import App
#
# def getArguments(argv):
#     debug = False
#     try:
#         opts, args = getopt.getopt(argv, 'ghf:d', ["debug"])
#     except getopt.GetoptError as e:
#         logging.error(traceback.format_exc())
#         print('run.py -d')
#         sys.exit(2)
#
#     for opt, arg in opts:
#         if opt in ("-d", "--debug"):
#             debug = True
#
#     return debug
#
#
# # Start point of the process
# if __name__ == "__main__":
#
#     parentdir = os.path.dirname(os.path.abspath(__file__))
#     sys.path.append(parentdir)  # Add to the path environment variable
#
#     debug = getArguments(sys.argv[1:])
#
#     if debug:
#         logging.basicConfig(level=logging.DEBUG,
#                             format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                             datefmt='%Y-%m-%d %H:%M')
#     else:
#         if not os.path.isdir('./log/'):
#             os.mkdir('./log/')
#         logging.basicConfig(level=logging.INFO,
#                             format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                             datefmt='%Y-%m-%d %H:%M', filename='./log/app.log', filemode='a')
#
#     # Create the project application
#     Application = App()
#
#     # Run the application
#     Application.run(Settings.instance().FLASK_HOST, Settings.instance().FLASK_PORT)
#

import os

from flask import Flask
from flask_assistant import Assistant, ask

app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('test')
def hello_world():
    speech = 'Microphone check 1, 2 what is this?'
    return ask(speech)


if __name__ == '__main__':
    app.run('0.0.0.0', int(os.getenv('PORT', 5000)), debug=True)
