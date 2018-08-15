import configparser


class Base(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("environment.ini")
        host_patient = config.get('base', 'protocol') + '://' + config.get('base', 'host_patient')
