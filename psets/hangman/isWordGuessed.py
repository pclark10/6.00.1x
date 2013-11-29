def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    count=0
    while count < len(lettersGuessed):
        if lettersGuessed[count] in secretWord:
            word += lettersGuessed[count]
        count+=1
    def checkWord(secretWord, word):
        if len(word)==0:
            return True
        if word[0] in secretWord:
            return checkWord(secretWord, word[1:])
        else:
            return False
    if len(word) == len(secretWord):
        return checkWord(secretWord, word)
    else:
        return False