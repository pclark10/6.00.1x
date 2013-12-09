from ps7 import *

koala = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')

s2  = TitleTrigger('')
s3 = TitleTrigger('koala')
print s2.evaluate(koala)

s4 = OrTrigger(s2, s3)
print s4.evaluate(koala)