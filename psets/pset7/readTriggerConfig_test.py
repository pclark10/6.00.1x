from ps7 import *

filename = 'C:/Users/kq195d/documents/github/6.00.1x/psets/pset7/phrase_triggers.txt'

readtrig = readTriggerConfig(filename)

#print readtrig

nasa = NewsStory('', 'NASA releases Curiosity Mars rover', '', '', '')

print nasa.getTitle()

print readtrig[3]

print readtrig[3].evaluate(nasa)