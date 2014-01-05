# -*- coding: utf-8 -*-
import ..exception

class Decode:
	def __init__(self, binary, eflags):
		raise exception._NotImplementedException("__init__")
	def meta(self, binary=None, eflags=None):
	""" Get meta-data, specifically tags """
		raise exception._NotImplementedException("meta")
	def decode(self, file):
	""" Do the decode, and where possible you PIPE (subprocess) to actually pass
	    the data stream to the encode processor.
	"""
		raise exception._NotImplementedException("decode")