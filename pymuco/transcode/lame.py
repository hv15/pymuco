# -*- coding: utf-8 -*-
import abc_transcode
import subprocess

EXTENSION = 'mp3'
BINARY = 'lame'

class Encode(abc_transcode.Encode):
    def __init__(self, eflags, binary = BINARY):
        self.binary = [binary]
        self.eflags = eflags.split()
        self.args = self.binary + self.eflags
    def meta(self):
        pass
    def encode(self, stream, outfile):
        return subprocess.Popen(self.args + [outfile], stdout=subprocess.PIPE, stdin=stream.stdout)
    def settings(self, outfile):
        print("ARGS: %s" % (self.args + [outfile]))
