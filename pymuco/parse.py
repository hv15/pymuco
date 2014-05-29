# -*- coding: utf-8 -*-
""""""
import argparse
import sys
import os
from distutils import spawn
# Local
import settings

class _ShowDefaults(argparse.Action):
    """"""
    def __init__(self,
        option_strings,
        dest=None,
        const=None,
        default=None,
        required=False,
        help=None,
        metavar=None):
        super(_ShowDefaults, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=0,
            const=const,
            default=default,
            required=required,
            help=help)
    def __call__(self, parser, namespace, values, option_string=None):
        defaults = settings.ReadSettings().defaults()
        print("  {:<10}  {}".format("FLAG", "VALUE"))
        for key, value in defaults.items():
            print("--{:<10}= {}".format(key, value))
        sys.exit(0)

class _FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

class ParseArguments():
    def __init__(self):
        self.defaults = settings.ReadSettings().defaults()
        self.parser = argparse.ArgumentParser(
                                        description="a PYthon MUsic COnverter",
                                        epilog="Created by Hans-Nikolai"
                                        " Viessmann, Copyright 2014")
    def _arguments(self):
        self.parser.add_argument('--format', default=self.defaults['format'],
                                 choices={'mp3','ogg'},
                                 help="output format (default: %(default)s)")
        self.parser.add_argument('--config', default=None,
                                help="use config file (default: settings.ini)")
        self.parser.add_argument('--lame', default=None,
                                help="LAME location (default: from PATH)")
        self.parser.add_argument('--flac', default=None,
                                help="FLAC location (default: from PATH)")
        self.parser.add_argument('--ogg', default=None,
                                help="oggenc location (default: from PATH)")
        self.parser.add_argument('--defaults', action=_ShowDefaults,
                                help="show default config")
        self.parser.add_argument('source', metavar='SRC', action=_FullPaths,
                                 help="source directoy")
        self.parser.add_argument('destination', metavar='DEST', action=_FullPaths,
                                 help="output directory")
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

class CheckDepends:
    def __init__(self, progs=['flac','lame','oggenc'], locs={}):
        self.progs = progs
        self.locs = locs
    def check(self):
        dic = {}
        for prog in self.progs:
            dic[prog] = self._which(prog)
            print("Found: {} at {}".format(prog, dic[prog]))
        return dic
    def _which(self, prog):
        if prog in self.locs:
            return self.locs[prog]
        fprog = spawn.find_executable(prog)
        if fprog:
            return fprog
        else:
            print("You seem to be missing `{}'! It is not in your PATH"
                  " variable. If you want you can specify it using the"
                  " appropriate command line flag. Call  `--help' for more"
                  " information".format(prog))
            return None

# Debugging
if __name__ == "__main__":
    pa = ParseArguments()
    p = pa.parse()
    cd = CheckDepends(locs=pa.locs(p))
    c = cd.check()
    print("FOUND: %s" % c)
    print("PARSED: %r" % p)
