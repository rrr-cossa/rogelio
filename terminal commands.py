import random
# List of words to choose from
print('python', 'java', 'javascript', 'ruby', 'html', 'css')
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
selected_word = random.choice(word_list)
# Guess a word of the list
guess = input('Choose a word from the list: ')
while True:
 
    if guess == selected_word:
        print('Your word is correct')
        break
    elif guess != selected_word:
        print('Your word is wrong')
        guess= input('Choose a word from the list: ')