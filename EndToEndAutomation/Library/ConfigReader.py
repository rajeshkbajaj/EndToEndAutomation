import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)

#print(readConfigData('Details','Application_URL'))

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)

#print(fetchElementLocators('Registration','username_name'))

# import os
# from pathlib import Path
# import configparser
#
# path = Path(__file__)
# ROOT_DIR = path.parent.absolute()
# config_path = os.path.join(ROOT_DIR, "Config.cfg")
# config = configparser.ConfigParser()
# config.read(config_path)