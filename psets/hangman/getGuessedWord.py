def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s1=''
    word=''
    count=0
    while count < len(lettersGuessed):
        if lettersGuessed[count] in secretWord:
            word += lettersGuessed[count]
        count+=1
    for x in range(len(secretWord)):
        if secretWord[x] in word:
            s1 += secretWord[x]
        else:
            s1 += '_ '
    return s1