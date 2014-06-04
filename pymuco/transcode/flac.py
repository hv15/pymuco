# -*- coding: utf-8 -*-
import subprocess
# Local
import abc_transcode

EXTENSION = 'flac'
BINARY = 'flac'

class Decode(abc_transcode.Decode):
    def __init__(self, eflags, binary = BINARY):
        self.binary = [binary]
        self.eflags = eflags.split()
        self.args = self.binary + self.eflags
    def meta(self):
        pass
    def decode(self, file):
        return subprocess.Popen(self.args + [file], stdout=subprocess.PIPE)
    def settings(self, infile):
        print("ARGS: %r" % (self.args + [infile]))
