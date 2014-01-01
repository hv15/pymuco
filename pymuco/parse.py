# -*- coding: utf-8 -*-
import argparse
import settings
import sys
from distutils import spawn

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
		print "FLAG         VALUE"
		for key, value in defaults.viewitems():
			print "--{0}: {1}".format(key, value)
		sys.exit(0)

class ParseArguments:
	def __init__(self):
		self.defaults = settings.ReadSettings().defaults()
		self.parser = argparse.ArgumentParser(description="a Python Music Converter", epilog="Created by Hans-Nikolai Viessmann")
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

class _ExecNotFound(Exception):
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
				dic[prog] = self._which(prog)
			return dic
		except _ExecNotFound as enf:
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
			raise _ExecNotFound(prog)

if __name__ == "__main__":
	pa = ParseArguments()
	p = pa.parse()
	cd = CheckDepends(locs=pa.locs(p))
	c = cd.check()