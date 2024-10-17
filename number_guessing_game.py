# number guessing game
# task is to Create a game where the computer randomly selects a number, and the user has to guess it within a limited number of tries.
import random

def number_guessing_game():

    #generate any number between 1 and 100
    number_tobe_guessed = random.randint(1,100)

    #no.of attempts to guess the number correctly { come on increase the number of attempts and try it if you are here }.
    attempts = 6

    print("welcome to number guessing game")
    print("i choosed a number now its your chance to make a correct guess")


    # checking guessed number

    for attempt in range(1, attempts+1):

        your_guess = int(input("enter the number you have guessed: "))

        if your_guess == number_tobe_guessed:
                         print("Your'e absolutely right!")
                         break
        elif your_guess < number_tobe_guessed:
            print("your guess is on lower side, make it up")

        else:
            print("your guess is on higher side")

        # after all attempts
        if attempt == attempts:
                  print(f"sorry you are out of chances. the number was {number_tobe_guessed}.")

number_guessing_game()                       
        
 
