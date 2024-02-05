import random
import hangmanwords

#Convert a list of letters into a word
def list_to_word(list):
    returnval = ""
    for letter in list:
        returnval += letter
    return returnval

#Convert a word into a list of letters
def word_to_list(word):
    returnval = []
    for letter in word:
        returnval.append(letter)
    return returnval

#Add spacing between letters of a word
def present_board(word):
    returnval = ""
    for letter in word:
        returnval += " " + letter + " "
    return returnval

#Update each occurence of letter in word on board
def update_board(letter, word, board):
    word_list = word_to_list(word)
    board_list = word_to_list(board)
    for letterindex in range(0, len(word_list)):
        if letter == word_list[letterindex]:
            board_list[letterindex] = letter
    return list_to_word(board_list)

#Define list of game words
words = hangmanwords.words

#Welcome player
print("Welcome to hangman!")

#Ask player for difficulty level
difficulty = int(input("Enter a difficulty level (1=Hard, 2=Normal, 3=Easy) "))

#Randomly choose a word from the game words list
word = random.choice(words)

#Game logic
#Instantiate game
rounds = len(word) + difficulty
round = rounds
playerhassolved = False
board = ""
for i in range(0, len(word)):
    board += "_"

#Loop so long as rounds remain and player has not solved the puzzle
while round > 0 and not(playerhassolved):
    #Inform player how many rounds remain
    print(f"{round} rounds remain to solve the puzzle.")
    #Output the current state of the board
    print(f"\n{present_board(board)}\n")
    #Ask user to enter a letter
    letter = input("Enter a letter: \n").lower()
    #Update the board based on the letter guessed
    board = update_board(letter, word, board)
    #Determine if the player has solved the puzzle
    if word == board:
        playerhassolved = True
    #Decrement the round counter
    round -= 1

#Inform player how many rounds remain
print(f"{round} rounds remain to solve the puzzle.")
#Output the current state of the board
print(f"\n{present_board(board)}\n")

#Output game result
#To win player must have guessed all the letters in the word
#and rounds remaining must be greater than or equal to zero
if round >= 0 and playerhassolved:
    print(f"You solved the puzzle with {round} rounds remaining and have not been hanged!")
else:
    print("You've run out of rounds before solving the puzzle and have been hanged!")