# -*- coding: utf-8 -*-
"""
Created on Thu May 29 21:36:37 2014

@author: Hans
@copyright: 2014
"""
import os

TRANSCODE = 'transcode'
TRANSCODERS = os.path.abspath(TRANSCODE)

class Transcoders(object):
    def __init__(self):
        self.encoders = []
        self.decoders = []
        self.plugins = []
    def find_transcoders(self, location=TRANSCODERS):
        self.plugins = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location,f)) and f.endswith('.py') and f != '__init__.py']
        for plugin in self.plugins:
            pak = plugin.split('.')[0]
            mod = __import__(TRANSCODE + "." + pak, fromlist = ['*'])
            if hasattr(mod, 'Decode'):
                self.decoders.append(pak)
            if hasattr(mod, 'Encode'):
                self.encoders.append(pak)

if __name__ == '__main__':
    t = Transcoders()
    t.find_transcoders()
    print("PLUGINS: ", t.plugins)
    print("DECODER: ", t.decoders)
    print("ENCODER: ", t.encoders)
