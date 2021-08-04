import random

number = random.randint(1, 10)

guesses = 0

print("I am guessing a number between 1 and 10...")
while guesses < 5:
    guess = int(input("Guess! "))
    guesses += 1
    
    if guess < number:
        print("Your guess is lower than my number")
    if guess > number:
        print("Your guess is higher than the my number")
    if guess > 10 or guess < 1:
        print("Please choose numbers in between 1 and 10")
    if guess == number:
        break
if guess == number:
    print(f"You guessed the number in {str(guesses)} tries!")
else:
    print(f"You didn't guess the number, the number was {str(number)}.")
