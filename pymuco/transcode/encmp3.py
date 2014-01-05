# -*- coding: utf-8 -*-
import ..exception
import subprocess
import encode

class EncMP3(encode.Encode):
	def __init__(self, binary, eflags):
		self.binary = binary
		self.eflags = eflags
	def meta(self, binary=None, eflags=None):
		pass
	def encode(self, stream):
		p = subprocess.Popen([self.binary, self.eflags], stdin=subprocess.PIPE)
		p.communicate(stream.communicate()[0])