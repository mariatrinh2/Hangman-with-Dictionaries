# imports random and time functions
import random
import time

# the hangman graphic
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

# Dictionary of Lists
# 4 categories user can select
words = {
    'fruits': ["cantulope", "strawberry", "apple", "orange", "banana",
               "peach", "apricot", "blackberry", "rasberry", "blueberry",
               "grapes", "papaya", "mango", "kiwi", "honeydew", "guava",
               "watermelon", "lemon", "cherry", "pineapple"],

    'pastas': ["manicotti", "bucatini", "tagliatelle", "ravioli", "gemelli", "farfalle",
               "fettuccine", "fiori", "cannelloni", "ditalini", "rotini", "linguine", "conchiglie",
               "radiatori", "pici", "garganelli", "vermicelli", "cavatappi", "tortellini",
               "pappardelle", "fusilli bucati", "lasagnette", "stringozzi", "risi", "paccheri"],

    'desserts': ["mint bars", "tiramisu", "pie", "banana pudding", "cheesecake",
                 "fudge", "funnel cake", "ice cream", "frozen yogurt", "creme brulee",
                 "cookie", "custard tart", "cinnamon roll", "flan", "brownie",
                 "cake ball", "blueberry muffin", "donuts", "cupcakes",
                 "fruitcake", "jelly roll", "ladyfinger", "cannoli", "cobbler",
                 "fritter", "gelato", "macaroon", "mousse", "tart"],

    'beverages': ["crush", "hawaiian punch", "coke zero", "v8", "fanta", "folgers",
                  "snapple", "minute maid", "welch's", "diet dr pepper", "tropicana",
                  "sunkist", "dole", "diet pepsi", "kool-aid", "7up", "mountain dew",
                  "lipton iced tea", "gatorade", "diet coke", "sprite", "pepsi",
                  "water", "lemonade", "apple juice"]
}
## Function Definitions ##


# prints hangman display board
# along with letters missed and letters guessed correctly
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


# selects random word from desired list
def randomWord(list):
    number = random.randint(1, 20)
    return list[number-1]


# checks if user's guess is a valid entery
# i.e. a single letter which has not been previously entered
def getGuess():
    while True:
        print("Guess a letter")
        guess = input()
        if not guess.isalpha():
            print("Opps! This is not a valid entery!")
            time.sleep(2)
            print("Please enter a letter from the alphabet.")
        elif len(guess) != 1:
            print("Opps! This is not a valid entery!")
            time.sleep(2)
            print("Please enter only ONE letter at a time.")
        elif guess in alreadyGuessed:
            print("You've already guessed this letter, silly! Try again :)")
        else:
            return guess


# asks user if they would like to play again
def playAgain():
    print("Would you like to play again? (Enter 'Yes' or 'No')")
    return input().startswith('y')


# game intro
print("What's your name stranger?")
name = input()
print("Nice to meet you " + name)
time.sleep(2)
print("Let's play a game!")
time.sleep(3)

# asks user to select a category to guess from
print("Enter a Category: fruits, pastas, desserts, or beverages")
pick = input()
if pick == 'fruits':
    list = words.get('fruits')
if pick == 'pastas':
    list = words.get('pastas')
if pick == 'desserts':
    list = words.get('desserts')
if pick == 'beverages':
    list = words.get('beverages')


print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord = randomWord(list)
gameDone = False


# loop which executes the game
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # identifies characters user has already entered
    alreadyGuessed = correctLetters + missedLetters
    guess = getGuess()
    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        # if all correct letters are guessed user wins :)
        if foundAllLetters:
            print("You win!")
            time.sleep(2)
            print('The secret word is "' + secretWord + '"')
            time.sleep(3)
            gameDone = True

    # checks if user's number of guesses are in range
    else:
        missedLetters += guess
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Oh no! You are out of guesses :(')
        time.sleep(2)
        print('After ' + str(len(missedLetters)) + ' missed guesses and ' +
              str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
        time.sleep(3)
        gameDone = True
    # asks user if they would like to play again
    # ask user which categories to pick from
    if gameDone:
        if playAgain():
            print("Enter a Category: fruits, pastas, desserts, or beverages")
            pick = input()
            if pick == 'fruits':
                list = words.get('fruits')
            if pick == 'pastas':
                list = words.get('pastas')
            if pick == 'desserts':
                list = words.get('desserts')
            if pick == 'beverages':
                list = words.get('beverages')
            missedLetters = ''
            correctLetters = ''
            gameDone = False
            secretWord = randomWord(list)
        else:
            break
