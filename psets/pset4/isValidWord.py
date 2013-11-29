def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    newhand = hand.copy()
    if word in wordList:
        for ltr in word:
            if ltr in newhand:
                newhand[ltr] -= 1
            else:
                return False
        else:
            return True
    else:
        return False