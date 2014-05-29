# -*- coding: utf-8 -*-
import abc_transcode
import subprocess

class Encode(abc_transcode.Encode):
    def __init__(self, binary, eflags):
        self.binary = [binary]
        self.eflags = eflags.split()
        self.args = self.binary + self.eflags
    def meta(self):
        pass
    def encode(self, stream, outfile):
        p = subprocess.Popen(self.args + [outfile], stdout=subprocess.PIPE, stdin=stream.stdout)
        stream.stdout.close()
        output = p.communicate()[0]
    def settings(self, outfile):
        print("ARGS: %s" % (self.args + [outfile]))
