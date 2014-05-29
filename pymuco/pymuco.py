# -*- coding: utf-8 -*-
import os
import shutil
# Local
import parse
from transcode import flac, mp3
import settings

DECODE = ('.flac')
OTHER = ('.jpg', '.jpeg', '.gif', '.png', '.log')

def klass(module, fromlist):
    """ dynamically import a class """
    mod = __import__(module, fromlist)
    return getattr(mod, fromlist)

def walk(input, output):
    print("Walking in %s -> %s" % (input, output))
    for root, dirs, files in os.walk(input):
        for name in files:
            if name.endswith(DECODE):
                # this is where we do the actual transcoding...
                print("Transcoding `%s'" % name)
                print("%s" % root)
                process(root, name, output)
            elif name.endswith(OTHER):
                print("Copying over `%s'" % name)
                shutil.copy(os.path.join(root, name), output)
        for name in dirs:
            output = os.path.join(output, name)
            if not os.path.isdir(output):
                os.mkdir(output)
                
def process(root, file, output):
    decoder = os.path.splitext(file)[1][1:]
    encoder = p.format
    (prefix, sep, suffix) = file.rpartition('.')
    ofile = os.path.join(output, prefix + '.mp3')
    d = flac.Decode(c[decoder], s.get('default', 'dflags'))
    e = mp3.Encode(c[encoder], s.get('default', 'eflags'))
    d.settings(os.path.join(root, file))
    e.settings(ofile)
    e.encode(d.decode(os.path.join(root, file)), ofile)

# parse command line flags and source file/directory
pa = parse.ParseArguments()
p = pa.parse()

# check decoder/encoder dependencies
cd = parse.CheckDepends(locs=pa.locs(p))
c = cd.check()

# setup settings
s = settings.ReadSettings()
s.open("settings.ini")

# Begin walking
if not os.path.isdir(p.destination):
    os.mkdir(p.destination)
walk(p.source, p.destination)