from ps7 import *

koala = NewsStory('', 'Koala bears are softand cuddly', '', '', '')

#s2  = TitleTrigger('')
#s3 = TitleTrigger('koala')
#print s2.evaluate(koala)
#
#s4 = OrTrigger(s2, s3)
#print s4.evaluate(koala)

s5 = PhraseTrigger('Koala bears are soft and')
print s5.evaluate(koala)