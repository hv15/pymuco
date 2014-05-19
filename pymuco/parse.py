# -*- coding: utf-8 -*-
import argparse
import sys
from distutils import spawn
# Local
import settings
import exception

class _ShowDefaults(argparse.Action):
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
		print ("  {:<10}  {}".format("FLAG","VALUE"))
		for key, value in defaults.items():
			print ("--{:<10}= {}".format(key, value))
		sys.exit(0)

class ParseArguments:
	def __init__(self):
		self.defaults = settings.ReadSettings().defaults()
		self.parser = argparse.ArgumentParser(description="a PYthon MUsic COnverter", epilog="Created by Hans-Nikolai Viessmann, Copyright 2014")
	def _arguments(self):
		self.parser.add_argument('--format', default=self.defaults['format'],
								help="output format (default: %(default)s)")
		self.parser.add_argument('--config', default=None,
								help="use config file (default: use defaults)")
		self.parser.add_argument('--lame', default=None,
								help="lame location (default: from PATH")
		self.parser.add_argument('--flac', default=None,
								help="flac location (default: from PATH")
		self.parser.add_argument('--ogg', default=None,
								help="oggenc location (default: from PATH")
		self.parser.add_argument('--defaults', action=_ShowDefaults,
								help="show default config")
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
		try:
			dic = {}
			for prog in self.progs:
				dic[prog] = self._which(prog)
			return dic
		except exception._ExecNotFound as enf:
			print ("You seem to be missing `{0}'! It is not in your PATH"
				   " variable. If you want you can specify it using the"
				   " appropriate command line flag. Call  `--help'"
				   " for more information".format(enf.value))
	def _which(self, prog):
		if prog in self.locs:
			return self.locs[prog]
		fprog = spawn.find_executable(prog)
		if fprog:
			return fprog
		else:
			raise exception._ExecNotFound(prog)

if __name__ == "__main__":
	pa = ParseArguments()
	p = pa.parse()
	cd = CheckDepends(locs=pa.locs(p))
	c = cd.check()
