import os
import yaml
import csv
import ast
import pandas
import logging
from shutil import copyfile
from pprint import pprint


class FileManager():
    parentdir = os.path.dirname(os.path.abspath(__file__))
    schemaPath = os.path.join(parentdir, 'schema')
    templatesPath = os.path.join(parentdir, 'templates')
    backupSchemaPath = os.path.join(os.path.join(parentdir, 'backup'), 'schema')
    backupTemplatePath = os.path.join(os.path.join(parentdir, 'backup'), 'templates')

    entitiesJsonPath = os.path.join(schemaPath, 'entities.json')
    intentsJsonPath = os.path.join(schemaPath, 'intents.json')
    entitiesYamlPath = os.path.join(templatesPath, 'entities.yaml')
    userSaysYamlPath = os.path.join(templatesPath, 'user_says.yaml')

    entitiesCsvPath = os.path.join(templatesPath, 'entities.csv')
    userSaysCsvPath = os.path.join(templatesPath, 'user_says.csv')
    entitiesXlsxPath = os.path.join(os.path.dirname(parentdir), 'Agent', 'entities.xlsx')
    userSaysXlsxPath = os.path.join(os.path.dirname(parentdir), 'Agent', 'user_says.xlsx')

    newEntitiesJsonPath = os.path.join(backupSchemaPath, 'entities.json')
    newIntentsJsonPath = os.path.join(backupSchemaPath, 'intents.json')
    newEntitiesYamlPath = os.path.join(backupTemplatePath, 'entities.yaml')
    newUserSaysYamlPath = os.path.join(backupTemplatePath, 'user_says.yaml')

    @staticmethod
    def saveBackupFiles():

        copyfile(FileManager.entitiesJsonPath, FileManager.newEntitiesJsonPath)
        copyfile(FileManager.intentsJsonPath, FileManager.newIntentsJsonPath)
        copyfile(FileManager.entitiesYamlPath, FileManager.newEntitiesYamlPath)
        copyfile(FileManager.userSaysYamlPath, FileManager.newUserSaysYamlPath)

    @staticmethod
    def updateYAMLtemplatesFromXLSX():
        FileManager._intentsXLSXtoYAML(FileManager.entitiesXlsxPath, FileManager.entitiesYamlPath)
        FileManager._userSaysXLSXtoYAML(FileManager.userSaysXlsxPath, FileManager.userSaysYamlPath)

    @staticmethod
    def _intentsXLSXtoYAML(xlsxPath, yamlPath):
        newDict = FileManager._readIntentsXLSXasDict(xlsxPath)
        FileManager._saveDictInYAML(newDict, yamlPath)

    @staticmethod
    def _userSaysXLSXtoYAML(xlsxPath, yamlPath):
        newDict = FileManager._readUserSaysXLSXasDict(xlsxPath)
        FileManager._saveDictInYAML(newDict, yamlPath)

    @staticmethod
    def _readIntentsXLSXasDict(xlsxPath):
        data = pandas.read_excel(xlsxPath)
        headers = list(data.to_dict())
        data = data.fillna(method='pad')
        data = data.applymap(lambda x: x.strip() if type(x) is str else x)
        data = data.transpose()
        excelDict = data.to_dict()

        newDict = dict()
        for key, value in excelDict.items():
            if not value[headers[0]] in newDict:
                newDict[value[headers[0]]] = dict()
            if not value[headers[1]] in newDict[value[headers[0]]]:
                newDict[value[headers[0]]][value[headers[1]]] = []
            newDict[value[headers[0]]][value[headers[1]]] = ast.literal_eval(value[headers[2]])

        return newDict

    @staticmethod
    def _readUserSaysXLSXasDict(xlsxPath):
        data = pandas.read_excel(xlsxPath)
        headers = list(data.to_dict())
        data = data.fillna(method='pad')
        data = data.applymap(lambda x: x.strip() if type(x) is str else x)
        data = data.transpose()
        excelDict = data.to_dict()

        newDict = dict()
        for key, row in excelDict.items():
            intent = row[headers[0]]
            if not intent in newDict:
                newDict[intent] = dict(UserSays=[], Annotations=[], Events=[])
            for phrase in ast.literal_eval(row['UserSays']):
                newDict[intent]['UserSays'].append(phrase)
            if not row['AnnotationValue'] in newDict[intent]['Annotations']:
                newDict[intent]['Annotations'].append({row['AnnotationParam']: row['AnnotationValue']})
            for event in ast.literal_eval(row['events']):
                newDict[intent]['UserSays'].append(event)

        return newDict

    @staticmethod
    def updateYAMLtemplatesFromCSV():
        FileManager._intentsCSVtoYAML(FileManager.entitiesCsvPath, FileManager.entitiesYamlPath)
        FileManager._userSaysCSVtoYAML(FileManager.userSaysCsvPath, FileManager.userSaysYamlPath)

    @staticmethod
    def _intentsCSVtoYAML(csvPath, yamlPath):
        newDict = FileManager._readIntentsCSVasDict(csvPath, ['entity', 'value', 'synonyms'])
        FileManager._saveDictInYAML(newDict, yamlPath)

    @staticmethod
    def _userSaysCSVtoYAML(csvPath, yamlPath):
        newDict = FileManager._readUserSaysCSVasDict(csvPath, ['intent', 'UserSays', 'Annotations', 'Events'])
        FileManager._saveDictInYAML(newDict, yamlPath)

    @staticmethod
    def _readIntentsCSVasDict(csv_file, headers):

        newDict = dict()
        try:
            with open(csv_file) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not row[headers[0]] in newDict:
                        newDict[row[headers[0]]] = {}
                    if not row[headers[1]] in newDict[row[headers[0]]]:
                        newDict[row[headers[0]]][row[headers[1]]] = []
                    newDict[row[headers[0]]][row[headers[1]]] = ast.literal_eval(row[headers[2]])
        except IOError as e:
            logging.error("I/O error: {0}".format(e))
        return newDict

    @staticmethod
    def _readUserSaysCSVasDict(csv_file, headers):

        newDict = dict()
        try:
            with open(csv_file) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not row[headers[0]] in newDict:
                        newDict[row[headers[0]]] = dict(UserSays=[], Annotations=[], Events=[])
                    newDict[row[headers[0]]][row[headers[1]]] = ast.literal_eval(row[headers[1]])
                    newDict[row[headers[0]]][row[headers[2]]] = ast.literal_eval(row[headers[2]])
                    newDict[row[headers[0]]][row[headers[3]]] = ast.literal_eval(row[headers[3]])
        except IOError as e:
            logging.error("I/O error: {0}".format(e))
        return newDict

    @staticmethod
    def SaveTemplatesCSV():
        entitiesYamlPath = os.path.join(FileManager.templatesPath, 'entities.yaml')
        entitiesCsvPath = os.path.join(FileManager.templatesPath, 'entities.csv')
        # userSaysYamlPath = os.path.join(FileManager.templatesPath, 'user_says.yaml')
        # userSaysCsvPath = os.path.join(FileManager.templatesPath, 'user_says.csv')
        FileManager._EntitiesYaml2csv(entitiesYamlPath, entitiesCsvPath)
        # FileManager._UserSaysYaml2csv(userSaysYamlPath, userSaysCsvPath)

    @staticmethod
    def _saveDictInYAML(newDict, yamlPath):
        with open(yamlPath, 'w') as y:
            yaml.dump(newDict, y, default_flow_style=False)

    @staticmethod
    def _EntitiesYaml2csv(yamlPath, csvPath):

        with open(yamlPath, 'rb') as y:
            j = yaml.load(y)
            entitiesDict = []
            for entityName, entityContent in j.items():
                for values in entityContent:
                    for valueName, valuesContent in values.items():
                        entitiesDict.append(dict(entity=entityName,
                                                 value=valueName,
                                                 synonyms=valuesContent))
            FileManager._writeDictToCSV(csvPath, ['entity', 'value', 'synonyms'], entitiesDict)

    @staticmethod
    def _writeDictToCSV(csv_file, csv_columns, dict_data):
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError as e:
            logging.error("I/O error: {0}".format(e))
        return
