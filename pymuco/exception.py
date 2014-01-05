# -*- coding: utf-8 -*-

class _NotImplementedException():
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "[Exception]: You have forgotten to implement `{0}'!".format(self.value)

class _ExecNotFound(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "[Exception]: `{0}' not in PATH variable!".format(self.value)