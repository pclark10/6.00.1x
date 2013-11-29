def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    result=''
    alpha=string.ascii_lowercase
    for x in range(len(alpha)):
        if alpha[x] not in lettersGuessed:
            result += alpha[x]
    return result