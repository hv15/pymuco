# -*- coding: utf-8 -*-
"""
Created on Thu May 29 21:36:37 2014

@author: Hans
@copyright: 2014
"""
import os, sys
# Local
import exception

TRANSCODE = 'transcode'
TRANSCODERS = os.path.abspath(TRANSCODE)

class Transcoders(object):
    def __init__(self):
        self.encoders = {}
        self.decoders = {}
        self.exts = {}
        self.plugins = []
        self.find_transcoders()
    def import_transcoder(self, name, location=TRANSCODE):
        return __import__(location + '.' + name, fromlist = ['*'])
    def find_transcoders(self, location=TRANSCODERS):
        self.plugins = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location,f)) and f.endswith('.py') and f != '__init__.py']
        for plugin in self.plugins:
            pak = plugin.split('.')[0]
            mod = self.import_transcoder(pak)
            if hasattr(mod, 'Decode'):
                self.decoders[getattr(mod, 'EXTENSION')] = pak
            if hasattr(mod, 'Encode'):
                self.encoders[getattr(mod, 'EXTENSION')] = pak
        self.exts = dict({v:k for k, v in self.encoders.items()}, **{v:k for k, v in self.decoders.items()})
    def get_extension(self, transcoder):
        if self.exts:
            try:
                return "." + self.exts[transcoder]
            except KeyError:
                raise exception._ExtensionIsMissinge(transcoder)
        else:
            raise exception._ClassNotFullyInitilised('Transcoders')

if __name__ == '__main__':
    t = Transcoders()
    #t.find_transcoders()
    print("PLUGINS: ", t.plugins)
    print("DECODER: ", t.decoders)
    print("ENCODER: ", t.encoders)
    print("ALL    : ", t.exts)
    sys.stdout.write("EXTENSN: ")
    for ext in t.exts.keys():
        sys.stdout.write("{} ".format(t.get_extension(ext)))
    print()
