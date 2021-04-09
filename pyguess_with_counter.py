# A simple number guessing game
# Could you make something cooler?

# Asking for number of players
player = int(input("Please key in the number of player/s: "))

number = 0

while number < player:

    number = number + 1

    print ("\nPlayer number %d are you ready!" % (number))

    import random

# Make n a random number between 1 and 99
    n = random.randint(1, 99)

# To count the number of tries
    count = 0

# Ask user to guess the number
    guess = int(input("\nEnter an integer from 1 to 99: "))

    while n != "guess":

        count = count + 1

        print
        if guess < n:
            print ("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print ("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            print ("\nyou guessed it!")
            break

    print ("\nWell Done! You guessed it in %d tries!" % (count))

