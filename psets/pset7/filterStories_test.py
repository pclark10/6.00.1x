from ps7 import *

pt = PhraseTrigger("New York City")
tt = TitleTrigger("New")
st = SummaryTrigger("York")
a = NewsStory('a', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('b', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('c', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('noa', "something something new york city", '', '', '')
nob = NewsStory('nob', '', "something something new york city", '', '')
noc = NewsStory('noc', '', '', "something something new york city", '')

triggers = [pt, tt, st]
stories = [a, b, c, noa, nob, noc]
filteredStories = filterStories(stories, triggers)
for i in range(len(filteredStories)):
    print filteredStories[i].getGuid()
#print filterStories(stories, st)