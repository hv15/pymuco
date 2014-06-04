# -*- coding: utf-8 -*-
import os, shutil
# Local
import settings

class Processing(object):
    def __init__(self, transcoders, encoder, source, destination):
        self.settings = settings.ReadSettings()
        self.transcoders = transcoders
        self.encoder_name = encoder
        self.encoder_ext = self.transcoders.get_extension(self.encoder_name)
        self.encoder_mod = self.transcoders.get_transcoder(self.encoder_name)
        self.encoder_flag = self.settings.get(self.encoder_name, 'flags')
        self.static_files = self.settings.get('default', 'static_files')
        self.source = source
        self.destination = destination
    def run(self):
        if not os.path.isdir(self.destination):
            os.mkdir(self.destination)
        self._walk()
    def _walk(self):
        print("Walking in %s -> %s" % (self.source, self.destination))
        for root, dirs, files in os.walk(self.source):
            for file in files:
                name, sep, ext = file.rpartition('.')
                if ext in self.transcoders.decoders.values():
                    self._process(ext, os.path.join(root, file), os.path.join(self.destination, name + self.encoder_ext))
                elif ext in self.static_files:
                    print("Copying over `%s'" % file)
                    shutil.copy(os.path.join(root, file), self.destination)
            for directory in dirs:
                self.destination = os.path.join(self.destination, directory)
                if not os.path.isdir(self.destination):
                    os.mkdir(self.destination)
    def _process(self, ext, original, output):
        decoder = self.transcoders.get_transcoder(ext, True)
        decoder_name = self.transcoders.stxe[ext]
        d = decoder.Decode(self.settings.get(decoder_name, 'flags'))
        e = self.encoder_mod.Encode(self.encoder_flag)
        d.settings(original)
        e.settings(output)
        dstream = d.decode(original)
        estream = e.encode(dstream, output)
    
        print("TRANSCODING `%s'" % original)
    
        dstream.stdout.close()
        output = estream.communicate()[0]

# Debugging
if __name__ == '__main__':
    import parse
    p = parse.ParseArguments().parse()
    pr = Processing(p.encoder, p.source, p.destination)
    pr.run()
    
