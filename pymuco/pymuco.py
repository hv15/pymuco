# -*- coding: utf-8 -*-
import os, shutil
# Local
import parse
import transcoders
import settings

def walk(input, output):
    print("Walking in %s -> %s" % (input, output))
    for root, dirs, files in os.walk(input):
        for name in files:
            ext = name.split('.')[1]
            if ext in ts.decoders:
                # this is where we do the actual transcoding...
                process(root, name, output)
            elif ext in s.get('default','static'):
                print("Copying over `%s'" % name)
                shutil.copy(os.path.join(root, name), output)
        for name in dirs:
            output = os.path.join(output, name)
            if not os.path.isdir(output):
                os.mkdir(output)

def process(root, file, output):
    prefix, sep, suffix = file.rpartition('.')
    ofile = os.path.join(output, prefix + eext)
    decoder = ts.import_transcoder(ts.decoders[suffix])
    d = decoder.Decode(s.get(ts.decoders[suffix], 'flags'))
    e = encoder.Encode(s.get(p.encoder, 'flags'))
    d.settings(os.path.join(root, file))
    e.settings(ofile)
    dstream = d.decode(os.path.join(root, file))
    estream = e.encode(dstream, ofile)

    print("TRANSCODING `%s'" % os.path.join(root, file))

    dstream.stdout.close()
    output = estream.communicate()[0]

# Main Setup
s = settings.ReadSettings()
ts = transcoders.Transcoders()
ts.find_transcoders()

# parse command line flags and source file/directory
pa = parse.ParseArguments()
p = pa.parse()

# get encoder
encoder = ts.import_transcoder(p.encoder)

# Get Encoder extension
eext = ts.get_extension(p.encoder)

# Begin walking
if not os.path.isdir(p.destination):
    os.mkdir(p.destination)
walk(p.source, p.destination)