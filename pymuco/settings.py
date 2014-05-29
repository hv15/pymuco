# -*- utf-8 -*-
"""Settings Module

This module handles the reading of a configuration file that includes settings
for both Pymuco and third-party applications.
"""
from configparser import ConfigParser
import transcoders
import os

class ReadSettings(object):
    def __init__(self, file='settings.ini'):
        self.file = file
        self.config = ConfigParser()
        self.open(self.file)
    def open(self, file):
        if os.path.isfile(file):
            self.config.read(file)
        elif file == 'settings.ini':
            print("You don't seem to have a default configuration file...")
            print("A new one has been created for you at `%s'" % file)
            self.config['default'] = {'encoder': 'lame',
                                      'static': '.jpg .jpeg .gif .png .log .cue',
                                      'nstatic': '.bak .ini'}
            self.config['lame'] = {'flags': '--vbr-new -V0 --silent -'}
            self.config['flac'] = {'flags': '-d -c -s'}
            self.config['oggenc'] = {}
            with open('settings.ini', 'w') as configfile:
                self.config.write(configfile)
        else:
            print("`%s' could not be opened!" % file)
            exit(100)
    def _map(self, sections):
        defaults = {}
        for section in sections:
            options = self.config.options(section)
            defaults[section] = {}
            for option in options:
                try:
                   defaults[section][option] = self.config.get(section, option)
                except:
                    print("It seems I found `%s' but it has no option" % option)
                    defaults[section][option] = None
        return defaults
    def settings_for_transcoder(self, transcoder):
        if self.config[transcoder]:
            return self.config.items(transcoder)
        else:
            return None
    def get(self, section, option):
        return self.config.get(section, option)
    def defaults(self):
        self.open("settings.ini")
        return self._map(self.config.sections())
        
# Debugging
if __name__ == '__main__':
    c = ReadSettings()
    d = c.defaults()
    print("{:<9}   {}\n--------    ----".format("SECTIONS", "KEYS"))
    for key, value in d.items():
        print("{:<9}-> {}".format(key, value))
    t = transcoders.Transcoders()
    t.find_transcoders()
    for encoder in t.encoders:
        print(encoder, " -> ", c.settings_for_transcoder(encoder))
    for decoder in t.decoders:
        print(decoder, " -> ", c.settings_for_transcoder(decoder))
