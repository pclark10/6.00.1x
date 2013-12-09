from ps7 import *

pt = PhraseTrigger("New York City")
tt = TitleTrigger("New")
st = SubjectTrigger("York")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')

triggers = [pt, tt]
stories = [a, b, c, noa, nob, noc]
print filterStories(stories, triggers)
#print filterStories(stories, st)