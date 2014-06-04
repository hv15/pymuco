# -*- coding: utf-8 -*-
"""
Created on Thu May 29 21:36:37 2014

@author: Hans
@copyright: 2014
"""
import os, sys

TRANSCODE = 'transcode'
TRANSCODERS = os.path.abspath(TRANSCODE)

class Transcoders(object):
    def __init__(self):
        self.encoders = {}
        self.decoders = {}
        self.all = {}
        self.exts = {}
        self.stxe = {}
        self.plugins = []
        self.load_transcoders()
    def import_transcoder(self, name, location=TRANSCODE):
        return __import__(location + '.' + name, fromlist = ['*'])
    def load_transcoders(self, location=TRANSCODERS):
        self.plugins = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f)) and f.endswith('.py') and f != '__init__.py']
        for plugin in self.plugins:
            pak = plugin.split('.')[0]
            mod = self.import_transcoder(pak)
            if hasattr(mod, 'Decode'): 
                self.decoders[pak] = getattr(mod, 'EXTENSION')
            if hasattr(mod, 'Encode'):
                self.encoders[pak] = getattr(mod, 'EXTENSION')
            self.all[pak] = mod
            self.exts[pak] = getattr(mod, 'EXTENSION')
            self.stxe[getattr(mod, 'EXTENSION')] = pak
       # self.exts = dict({v:k for k, v in self.encoders.items()}, **{v:k for k, v in self.decoders.items()})
    def get_extension(self, name):
        """Returns the appropriate extension for a given transcoder, including
        the seporator (period: `.').
        """
        return "." + self.exts[name]
    def get_transcoder(self, name, extension=False):
        if extension:
            return self.all[self.stxe[name]]
        else:
            return self.all[name]

if __name__ == '__main__':
    t = Transcoders()
    #t.load_transcoders()
    print("PLUGINS: ", t.plugins)
    print("DECODER: ", t.decoders)
    print("ENCODER: ", t.encoders)
    print("EXTENSN: ", t.exts)
    print("NSNETXE: ", t.stxe)
    sys.stdout.write("EXTENSN:  ")
    for ext in t.exts.keys():
        sys.stdout.write("{} ".format(t.get_extension(ext)))
    print()
    print("MODS   : ", t.all)
    sys.stdout.write("MODS   :  ")
    for mod in t.all.values():
        sys.stdout.write("{} ".format(mod))
    print()
    sys.stdout.write("GETMODS:  ")
    for mod in t.exts.keys():
        sys.stdout.write("{} ".format(t.get_transcoder(mod)))
    print()
    sys.stdout.write("MODSGET:  ")
    for mod in t.exts.values():
        sys.stdout.write("{} ".format(t.get_transcoder(mod, True)))
    print()
