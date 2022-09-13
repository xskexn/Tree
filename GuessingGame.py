import random
guess = None
tryGuess = 0
outOfTry = False
randomNum = random.randint(0,10)
# print(randomNum) //Try it out if you think that my program 
# Is broken or you want to cheat 
print("Hi Welcome to the guessing game!")
while guess != randomNum and tryGuess <= 4 and not outOfTry:
    guess = int(input("Input a number between 0 and 10: "))
    if guess == randomNum:
        print("You made it in " + str(tryGuess) + " attempt")
        print("You Won!")
    elif tryGuess >= 5 and guess != randomNum:
        outOfTry = True
        print("Bruh You Lose sorry dude!")
    else:
        tryGuess += 1
        print("Try again!")
        print("Used " + str(tryGuess) + " guess out of 5" )