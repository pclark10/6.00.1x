# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    atme = atMe.myName()
    newfrob = newFrob.myName()
    if min(newfrob, atme) == atme:
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
    else:
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)