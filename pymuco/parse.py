# -*- coding: utf-8 -*-
""""""
import argparse, os
from distutils import spawn
# Local
import settings

# Default configuration
DEFAULT_CONFIG = settings.ReadSettings().defaults()

class _ShowDefaults(argparse.Action):
    """"""
    def __call__(self, parser, namespace, values, option_string=None):
        print("{:<9}   {}\n--------    ----".format("SECTIONS", "KEYS"))
        for key, value in DEFAULT_CONFIG.items():
            print("{:<9}-> {}".format(key, value))
        exit(0)

class _FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

class ParseArguments(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                                        description="a Python music converter",
                                        epilog="Created by Hans-Nikolai"
                                        " Viessmann, Copyright 2014")
    def _arguments(self):
        self.parser.add_argument('--encoder',
                                 default=DEFAULT_CONFIG['default']['encoder'],
                                 choices={'lame','oggenc'},
                                 help="output encoder (default: `%(default)s')")
        self.parser.add_argument('--config-file', default='settings.ini',
                                help="use config file (default: %(default)s)")
        self.parser.add_argument('--defaults', action=_ShowDefaults, nargs=0,
                                help="show default configuration")
        self.parser.add_argument('source', metavar='SRC', action=_FullPaths,
                                 help="source directoy")
        self.parser.add_argument('destination', metavar='DEST', action=_FullPaths,
                                 help="output directory")
    def parse(self):
        self._arguments()
        return self.parser.parse_args()

class CheckDepends:
    def __init__(self, progs=['flac','lame','oggenc']):
        self.progs = progs
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
    #cd = CheckDepends(locs=pa.locs(p))
    #c = cd.check()
    #print("FOUND: %s" % c)
    print("PARSED: %r" % p)
