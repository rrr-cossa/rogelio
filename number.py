import random

number = random.randint(1,10)
my_number = input('Choose a number between 1 to 10 (if you want to exit write "quit"): ')
while True:
    guess = int(my_number)
    if my_number == "quit":
        break
    
    else:
        if guess == number:
            print('Your guess is correct')
            break
        elif guess < number:
            print('Your number is to low')
            my_number=int(input('Guess a number between 1 to 10: '))
        elif guess > number:
            print('Your guessing to high')
            my_number=int(input('Guess a number between 1 to 10: '))
        elif guess > 10:
            print('Write number between 1 to 10')
            my_number=int(input('Guess a number between 1 to 10: '))