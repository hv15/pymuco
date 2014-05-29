# -*- coding: utf-8 -*-
"""Transcode <<abstract>>

This module contains the abstract classes `Decode' and `Encode' that are used
by transcode plugins to add new supported formats.
"""
import abc

class Decode(object):
    """Object that contains a single instance of a decode process."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def meta(self):
        """Get meta-data, specifically tags."""
        return

    @abc.abstractmethod
    def decode(self, file):
        """Do the decode, and where possible you PIPE (subprocess) to actually
        pass the data stream to the encode processor."""
        return

class Encode(object):
    """Object that contains a single instance of a encode process."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def meta(self, binary=None, eflags=None):
        """Apply meta-data, specifically tags."""
        return

    @abc.abstractmethod
    def encode(self, file):
        """From the decode process get the byte-stream and encode it."""
        return
