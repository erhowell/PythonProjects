import random
''' create a hangman game'''

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
   +---+
    O   |
   /|\  |
   / \  |
       ===''']

class RandomWordGenerator:
    def __init__(self):
       #create a list of words from words.txt
       #self.words = list of words from file.txt
       pass
    
    def getRandomWord(self):
        # return a random word from self.words
        pass 



class HangmanGame():
    def __init__(self, word):
        pass
        # self.word = word
        # self.wordRevealed =  # list or string with a length of word and each index is either a letter revealed or _ if the letter hasn't been guessed
        # self.maxMistakes =  # number of mistakes allowed before game over
        # self.mistakeCount = len(HANGMAN_PICS)-1
        # self.lettersGuessed =  # list of all letters guessed
        # self.gameOver = # indicates if game is over
        # self.guessedLetter = #the most reccent user input

    def getLetter(self): 
        # get letter input and check if input is valid
        # user must only enter 1 letter at a time, guess must be a letter, and not already guessed
        pass

    def checkLetterInWord(self):
        #check to see if guessed letter is in word
        #if guessedLetter is in word then replace spaces in wordRevealed with guessedLetter
        # if not then up mistake count
       pass

    def checkGameOver(self):
        # check to see if won or lost.
        # If won or lost game over is True
        pass
    
    def outPutBoard(self):
        #must show letters already guessed, the hangman pics, and word reavealed 
        #also any text to indicate if game is over and won or lost
        pass
    
    def gamePlay(self):
        while not self.gameOver:
            self.getLetter()
            self.checkLetterInWord()
            self.checkGameOver()
            self.outPutBoard()


continuePlay = True
randomWords = RandomWordGenerator()

def continuePlayPrompt():
    continuePlayInput = input("\bdo you want to keep playing? 1-yes 2-no")
    if continuePlayInput.isnumeric() and int(continuePlayInput) in [1,2]:
        if int(continuePlayInput) == 1:
            return True
        else:
            return False
    return continuePlayPrompt()

while continuePlay:
    word =randomWords.getRandomWord()
    game = HangmanGame(word)
    game.gamePlay()
    continuePlay= continuePlayPrompt()
    



