# -*- coding: utf-8 -*-

class _NotImplementedException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "[Exception]: You have forgotten to implement `{0}'!".format(self.value)

class _ExecNotFound(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "[Exception]: `{0}' not in PATH variable!".format(self.value)

class _ExtensionIsMissinge(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ("[Exception]: An extension for transcoder `{}' was not found! "
                "It is likely that the plugin is missing the correct definition, "
                "have a look at the EXTENSION variable...").format(self.value)

class _ClassNotFullyInitilised(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "[Exception]: Class `{}' has not been fully initilised!".format(self.value)
