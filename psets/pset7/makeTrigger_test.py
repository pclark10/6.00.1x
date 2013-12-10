from ps7 import *

triggers = []
triggerMap = {}

#SubjectTrigger('world').join(triggerMap['t1'])
#
#print triggerMap['t1']

trigger = makeTrigger(triggerMap, 'PHRASE', 'Curiosity Mars rover', 't1')

print trigger



print trigger.evaluate('is there Curiosity')