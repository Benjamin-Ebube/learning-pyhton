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

#help = "start - to start the car\nstop - to stop the car\nquit - to exit the game"
#start = 'your car has started!'
#stop = 'your car has stopped'
#print('welcome')
#while True:
#    response = input('> ').lower()
#    if response == 'help':
#       print(help)
#    elif response == 'start':
#        print(start)
#    elif response == 'stop':
#        print(stop)
#   elif response == 'quit':
#        exit()
#    else:
#     print('Sorry i dont understand that. Try "help" for the instruction manual.')


#learning "for" loops
#prices = [10, 20, 30]
# to calculate the total of the amount of properties in your shopping cart
#total = 0
#for price in prices:
#    total = total + price
#    print(f"Total: {total}")


# this is to remove duplicates
#numbers = [4, 6, 7, 2, 4, 9, 5, 0, 0]
#unique = []
#for values in numbers:
#    if values not in unique:
#        unique.append(values)
#print(unique)

# back to 'tuples' again. For tuples they are immutable('cant be changed')
#tuple_example = (1, 2, 4, 'howard', 9 )
#print(tuple_example)
# tuples are like lists just that they cant be modified.

# boutta show an example of 'unpacking' using tuples
#coordinates = (2, 6, 9, 'laps')
# this is a better way of assigning each item to a variables.
#a, b, c, d = coordinates
#print(a)
#print(b)
#print(c)
#print(d)
# it also works on lists too.


# learning about dictionaries now. THEY make use of key values.
#customer = {
#    'name': 'benjamin',
#    'age': 16,
#    'innocent': True
#}
#print(customer['name'])
# you can also use the get function to do it also
#print(customer.get('age'))



# learning about functions still...
# You use "def" meaning  to define functions.
#def greet_user():
#    print('hi')
#    print('welcome to my channel.')


#print('start')
#greet_user()
#print('it is done.')
# so basically the greet user just turns whatever has been written there into a function re-usable anytime.
# you can also define your functions using parameters. they are defined inside the closed brackets
#def biscuit(name):
#    print(f'Yo, I love {name}')
#    print('do you have some?')


#now you define the parameters you have given
#print("hows'it going broskis")
#biscuit('munch it')
#print('please!!!!!!')
# you can also define more than one parameter in it, just add a comma after the first parameter.

# learning about return statements...they are used mostly in calculations.
#def square(number):
#    return number * number
#print(square(6))
# By default all functions will 'return' "none", but you can change that by using the return statement.



# learning about 'try' and 'except' values.
# try and except blocks are used to handle exceptions raised in our programs.

#try:
#    age = int(input('age: '))
#    print(age)
#except ValueError:           #this is an exception for if the person inputs the wrong value.
#    print("Invalid value.")

#print('pick a number to divide my hidden number;')
#try:
#    key_value = int(input())
#    example = 108/key_value
#    print(example)
#except ZeroDivisionError:
#    print('you cant divide a number with zero!')


