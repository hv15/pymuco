# -*- coding: utf-8 -*-
import ..exception
import decode
import subprocess

class DecFLAC(decode.Decode):
	""" General decode system using subprocess's Popen function """
	def __init__(self, binary, eflags):
		self.binary = binary
		self.eflags = eflags
	def meta(self):
		pass
	def decode(self, file):
	""" Return a processes and its pipe information """
		return subprocess.Popen([self.binary, self.eflags, file], stdout=subprocess.PIPE)