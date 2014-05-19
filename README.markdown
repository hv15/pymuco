A *Python Music Converter*
==========================

        ______  __                         
       / __ \ \/ /___ ___  __  ___________ 
      / /_/ /\  / __ `__ \/ / / / ___/ __ \
     / ____/ / / / / / / / /_/ / /__/ /_/ /
    /_/     /_/_/ /_/ /_/\__,_/\___/\____/

About
-----

*Still in alpha-stage development*

**PYmuco** provides an easy way to effectively convert one's music library
(made up of a variety of files and formats) to a lossy format while still
preserving directory structure and static files like images. The script makes
use of tools created and provided by [LAME][lame], [FLAC][flac], [OGG][ogg],
etc.

### Requirements

    Needs Python 3 to run
    As a minimum, one should have the following binaries
      - FLAC (for decoding)
      - LAME (for encoding)

Goals
-----

 * Convert any (compatible?) audio format to mp3 or ogg
 * Recursively copy over all static content from current directory structure,
   including images
 * Apply ReplayGain onto newly created mp3
 * If missing (or required), apply IDv2/3 with latest records from freetag
 * Rename directories/files (based upon specified format)

Why
---

I have used several scripts, be they Shell, Python, or Ruby based to batch
convert files to mp3, however all of them have been clunky to say the least. I
want to create something structured and powerful to use. As simple as typing in
`pymuco . /newdir`, and it just works. I have been working a lot with Python
over the last few months, and think I have a good understand of how to make
this application.

Pronunciation
-------------

Ha, really?

License
-------

Currently there is no license used, however normal copyright still applies.

[lame]: http://lame.sourceforge.net/ "LAME MP3 Encoder"
[flac]: https://xiph.org/flac/ "free lossless audio codec"
[ogg]: http://www.xiph.org/ogg/ "The OGG container format"
