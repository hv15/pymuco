# -*- coding: utf-8 -*-
import ..exception

class Encode:
	def __init__(self, binary, eflags):
		raise exception._NotImplementedException("__init__")
	def meta(self, binary=None, eflags=None):
	""" Apply meta-data, specifically tags """
		raise exception._NotImplementedException("meta")
	def encode(self, file):
	""" From the decode process get the byte-stream and encode it """
		raise exception._NotImplementedException("decode")