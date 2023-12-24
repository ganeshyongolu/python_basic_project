import random #bring in the random number
import time
number=random.randint(1, 300) #pick the number between 1 and 300


def get_to_know():
    print("May I know your name?")
    name=input() #asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 300")
    time.sleep(.5)
    print("Go ahead. Guess!")
    return name


def pick_num(name):
    guessesTaken = 0
    while guessesTaken < 10: #if the number of guesses is less than 10
        time.sleep(.25)
        enter=input("Guess: ") #inserts the place to enter guess
        try: #check if a number was entered
            guess = int(enter) #stores the guess as an integer instead of a string    

            if guess<=300 and guess>=1: #if they are in range
                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong
                if guessesTaken<10:
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess==number:
                    break #if the guess is right, then we are going to jump out of the while block
            if guess>300 or guess<1: #if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 300")

        except: #if a number wasn't entered
            print("I don't think that "+enter+" is a number. Sorry")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    name = get_to_know()
    pick_num(name)
    print("Do you want to play again?")
    playagain=input("Enter yes/No:")