The **Ultimate Ruby Audio Converter**
=====================================

       __  __
      / / / /______  ______ ___  __  ___________
     / / / / ___/ / / / __ `__ \/ / / / ___/ __ \
    / /_/ / /  / /_/ / / / / / / /_/ / /__/ /_/ /
    \____/_/   \__,_/_/ /_/ /_/\__,_/\___/\____/

Goals:

 * Convert any (compatible?) audio format to mp3 or ogg
 * Recursively copy over all static content from current directory structure,
   including images
 * Apply ReplayGain onto newly created mp3
 * If missing (or required), apply IDv2/3 with latest records from freetag
 * Rename directories/files

Why:

I have used several scripts, be they BASH or Python, to batch convert files to
mp3, however all of them have been clunky to say the least. I want to create
something structured and powerful to use. As simple as typing in
`urumuco . /newdir`, and it just works. I have been working a lot with Ruby over
the last few months, and think I have a good understand of how to make this
app.

Pronounciation: Ha, really?
