# -*- coding: utf-8 -*-
import parse, processing, transcoders

if __name__ == '__main__':
    t = transcoders.Transcoders()
    p = parse.ParseArguments(t).parse()
    r = processing.Processing(t, p.encoder, p.source, p.destination)
    r.run()
