from currencyConverter import clearScreen
from random import seed, randint
from time import time
def counterLives(lives):
    """
    Shows a health bar according to your play.
    lives --> int: How many opportunities you still have to guess the word
    """
    if lives > 0:
        print("Lives: "+"♥"*lives)
    else:
        print("You are dead")


def verifyMatch(word,given):
    """
    Compare the given letter with the word you want to guess and update the hint
    word --> str: The word you can to guess
    given --> str: The letters the player has written
    return clue --> str: how is the player doing with the game
    """
    print(f"Given: {given}")
    clue = ["_" for i in range(len(word))]
    for i in given:
        if i in word:
            for j in range(len(word)):
                if i == word[j]:
                    clue[j] = i
    return clue


def main():
    options = ("vampire","destroyer","winner","competition","hangman","obstacle")
    seed(time())
    lives = 6
    word = options[randint(0,len(options)-1)]
    game = [" "]
    flag = True
    while(flag):
        letter = ' '
        clue = verifyMatch(word,game)
        for w in clue:
            print(w, end="")
        print()
        counterLives(lives)
        if lives <= 0:
            break
        if '_' in game:
            print(f"You have won the game, the word was: {word}")
            break
        while(letter in game):
            letter = input("Type a letter for the hangman:")
        game.append(letter)
        if letter not in word:
            lives -=1
        clearScreen()
    print("Hope you enjoyed the game")
        




if __name__ == "__main__":
    main()