import os
import appdirs
import yaml

appVersion = (0, 0, 1)
appVersionStr = '.'.join(map(str, appVersion))

def getConfigPath():
    path = appdirs.user_data_dir('OpenPep', 'OpenPep')
    if not os.path.isdir(path):  # Create directory if it doesn't exist
        os.mkdir(path)
    return path + '/'

def saveFile(path, data, dataType):
    output = {
        'version': appVersion,
        'type':dataType,
        'data': data
    }

def loadFile(path, dataType):
    pass

