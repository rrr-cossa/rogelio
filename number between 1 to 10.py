my_number = random.rendint(1,10)

guess = int (input('chose a number between 1 and 10'))
while True:
    try:
    if guess == my_number:
        print ('Congrats, you have the correct answer')
        break
    elif guess > my_number:
        print('your number is to high')
        guess = int (input('stay in the range 1 to 10')
    elif guess < my_number:
        print
