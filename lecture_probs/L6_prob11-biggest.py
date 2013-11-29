animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict)==0:
        return None
    maxLen=0
    for i in aDict:
        if len(aDict[i]) > maxLen:
            maxLen = len(aDict[i])
            big = i
        elif len(aDict[i]) <= 1:
            big=i
    return big