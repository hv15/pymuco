# -*- utf-8 -*-
from configparser import ConfigParser

class ReadSettings:
    def __init__(self):
        self.config = ConfigParser()
    def open(self, file):
        self.config.read(file)
    def map(self, section):
        dict = {}
        options = self.config.options(section)
        for option in options:
            try:
               dict[option] = self.config.get(section, option)
            except:
                print ("It seems I found `%s' but it has no option" % option)
                dict[option] = None
        return dict
    def get(self, section, option):
        return self.config.get(section, option)
    def defaults(self):
        self.open("settings.ini")
        return self.map("default")
