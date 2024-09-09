import random
options =["rock","paper","scissors"]

while True:
    user_ch = input('Chose rock, paper or scissors: ')
    cpu_ch = random.choice(options)
    
    if user_ch == "quit":
        break
        
    if user_ch == "ball":
        print("not allowed")
        continue
    
    if user_ch == cpu_ch:
        print("Tie")
    elif(user_ch == "rock" and cpu_ch == "scissors") or (user_ch == "paper" and cpu_ch == "rock") or (user_ch == "scissors" and cpu_ch == "paper"):
        print("You win!")
    else:
        print("You lost")