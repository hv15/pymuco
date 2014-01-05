# -*- coding: utf-8 -*-
import exception
import parse
import os
import shutil

CLASSES = {'flac':['transcode.decflac', 'DecFLAC'],
			'mp3' : ['transcode.encmp3', 'EncMP3']}
DECODE = ('.flac')
OTHER = ('.jpg', '.jpeg', '.gif', '.png')

def klass(name, fromlist):
	""" dynamically import a class """
	mod = __import__(name, fromlist)
	return getattr(mod, comp)

def walk(input, output):
	for root, dirs, files in os.walk(input):
		for file in files:
			if file.endwith(DECODE):
				# this is where we do the actual transcoding...
			elif file.endwith(OTHER):
				shutil.copy(os.path.join(root, file), output)
		for dir in dirs:
			walk(os.path.join(root, dir), output)

# parse command line flags and source file/directory
pa = parse.ParseArguments()
p = pa.parse()

# check decoder/encoder dependencies
cd = parse.CheckDepends(locs=pa.locs(p))
c = cd.check()

