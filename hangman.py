import random
print('''
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
''')
words = input("Welcome to Hangman! Type in the words that you would like me to pick from when we play.\n")
if words == '':
    words = input("Please tell me the words that you want.")
print("You have unlimited tries to guess my word")
wrds = words.split()
player = False

computer = random.choice(wrds)

while player == False:
    wrd1 = input("Guess my word('quit' for quit, 'hint' for hint, 'reset' for resetting words)")
    if wrd1 == "quit":
        print("Thanks for playing!")
        break
    elif wrd1 == "hint":
        print("My word is %s letters long" % (len(computer)))
    elif wrd1 == "reset":
        words = input("Please tell me the words that you want.")
        wrds = words.split()
        computer = random.choice(wrds)
        print("Alright, got it!")
    elif wrd1 != computer and not "hint":
        print("Wrong!")
    elif wrd1 == computer:
        g = input("You guessed it! Want to play again?(y/n)")
        computer = random.choice(wrds)
        if g == "y":
            continue
        elif g == "n":
            print("We will play later, bye!")
            break
        elif g != "y" or "n":
            print("What?")
            h = input("Would you like to play again or no?(y/n)")
            if h == "y":
                continue
            elif h == "n":
                print("Ok cool, bye!")
                break