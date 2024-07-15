# you can use formatted strings to be able to easily visualize code.
#first = 'john'
#last = 'smith'
# the formatted strings start with an 'f' and you use curly braces for variables.
#message = f'{first} [{last}] likes  apples.'
#print(message)

# 'len' is a function which is used in counting number of items either in a list or...ya know
#count_me = 'how many letters are here?'
#print(len(count_me))

#name_character =input('please enter your name\n')
#number = len(name_character)
#if number < 3:
#    print('name too short')
#elif number > 10:
 #   print('name too long')
#else:
#    print('thank you.')

#weight = int(input('please enter your weight;\n'))

#statement = input(f'({"L"})bs or ({"K"})gs\n')
#if statement.upper() == 'L':
 #   converted = weight * 0.45
  #  print(f'you are {converted} kilos.')
#elif statement.upper() == 'K':
#    pounds = weight * 45
#    print(f'you are {pounds} pounds.')
#else:
#    print('which planet did you come from bruv?')


# learning about while loops now.
#number = 1
#while number <= 5:
#    print(number)
#    number = number + 1
#print('finally done')

#boutta make a gamee using while loop!
#secret_number = 8
#guess_count = 0
#guess_limit = 4
#while  guess_count < guess_limit:
#    guess = int(input('guess: '))
#    guess_count = guess_count + 1
#    if guess == secret_number:
#        print('yay! you won.')
#        break
#else:
#    print('sorry, you failed.  :<')


#boutta build a car game ya'll

help = "start - to start the car\nstop - to stop the car\nquit - to exit the game"
start = 'your car has started!'
stop = 'your car has stopped'
print('welcome')
attempts = 0
trials = 10
while attempts < trials:
    response = input('> ')
    attempts = attempts + 1
    if response == 'help':
       print(help)
    elif response == 'start':
        print(start)
    elif response == 'stop':
        print(stop)
    elif response == 'quit':
        exit()
    else:
     print('Sorry i dont understand that. Try "help" for the instruction manual.')
