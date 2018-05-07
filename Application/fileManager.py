import os
import yaml
import csv


class FileManager():
    parentdir = os.path.dirname(os.path.abspath(__file__))
    templatesPath = os.path.join(parentdir, 'templates')

    @staticmethod
    def SaveTemplatesCSV():
        print(FileManager.templatesPath)
        entitiesYamlPath = os.path.join(FileManager.templatesPath, 'entities.yaml')
        entitiesCsvPath = os.path.join(FileManager.templatesPath, 'entities.csv')
        userSaysYamlPath = os.path.join(FileManager.templatesPath, 'user_says.yaml')
        userSaysCsvPath = os.path.join(FileManager.templatesPath, 'user_says.csv')
        FileManager._CopyYaml2csv(entitiesYamlPath, entitiesCsvPath)
        FileManager._CopyYaml2csv(userSaysYamlPath, userSaysCsvPath)

    @staticmethod
    def loadCSV(yamlPath, csvPath):
        pass

    @staticmethod
    def _CopyYaml2csv(yamlPath, csvPath):
        with open(yamlPath, 'rb') as y:
            j = yaml.load(y)
            with open(csvPath, 'ab+') as f:
                w = csv.DictWriter(f, j.keys(), dialect='excel')
                for element in j:
                    w.writerow(element)

    @staticmethod
    def _CopyCsv2yaml(yamlPath, csvPath):
        pass
