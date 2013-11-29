# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print '-------------'
    count=8
    lettersGuessed=''
    congrats='Congratulations, you won!'
    sorry='Sorry, you ran out of guesses. The word was'+secretWord+'.'
    while count > 0:
        print 'You have', count, 'guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter:').lower()
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print 'Good guess: '+getGuessedWord(secretWord,lettersGuessed)
        elif guess in lettersGuessed:
            print "Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed)
        else:
            lettersGuessed += guess
            print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord,lettersGuessed)
            count-=1
        print '-------------'
        if getGuessedWord(secretWord,lettersGuessed) == secretWord:
            return congrats
    return sorry


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'else'  #chooseWord(wordlist).lower()
hangman(secretWord)
