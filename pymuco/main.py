# -*- coding: utf-8 -*-
"""
@author: Hans
"""
import argparse
from distutils import spawn


class ParseArguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                                description="a Python Music Converter",
                                epilog="Created by Hans-Nikolai Viessmann")
    def _arguments(self):
        self.parser.add_argument('--format', default='mp3',
                                 help="ouput format (default: %(default)s)")
        self.parser.add_argument('--config', default=None,
                                 help="use config file (default: %(default)s)")
        self.parser.add_argument('--lame', default=None,
                                 help="lame location (default: %(default)s")
        self.parser.add_argument('--flac', default=None,
                                 help="flac location (default: %(default)s")
        self.parser.add_argument('--ogg', default=None,
                                 help="oggenc location (default: %(default)s")
    def parse(self):
        self._arguments()
        return self.parser.parse_args()
    def locs(self, parsed):
        dic = {}
        if parsed.flac:
            dic['flac'] = parsed.flac
        if parsed.lame:
            dic['lame'] = parsed.lame
        if parsed.ogg:
            dic['oggenc'] = parsed.ogg
        return dic


class ExecNotFound(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "[Exception]: `{0}' not in PATH variable!".format(self.value)


class CheckDepends:
    def __init__(self, progs=['flac','lame','oggenc'], locs={}):
        self.progs = progs
        self.locs = locs
    def check(self):
        try:
            dic = {}
            for prog in self.progs:
                dic[prog] = self.which(prog)
            return dic
        except ExecNotFound as enf:
            print ("You seem to be missing `{0}'! It is not in your PATH"
                   " variable. If you want you can specify it using the"
                   " appropriate commandline flag. See help (--help)"
                   " for more information".format(enf.value))
    def which(self, prog):
        if prog in self.locs:
            return self.locs[prog]
        fprog = spawn.find_executable(prog)
        if fprog:
            return fprog
        else:
            raise ExecNotFound(prog)

pa = ParseArguments()
p = pa.parse()
cd = CheckDepends(locs=pa.locs(p))
c = cd.check()