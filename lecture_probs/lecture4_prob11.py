def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    result = bool(char in 'aeiouAEIOU')
    return result
