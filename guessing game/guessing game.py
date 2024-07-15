print('Welcome to my guessing game.\nYou have 4 trial to guess a number between 1-10.\nIf not you have failed.')
print('good luck :>')
secret_number = 8
guess_count = 0
guess_limit = 4
while  guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count = guess_count + 1
    if guess == secret_number:
        print('yay! you won.')
        break
    elif guess != secret_number:
        print('wrong! :<')

else:
    print('sorry, you failed.  :<')