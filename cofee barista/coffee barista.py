print('Hello friend, welcome to my coffee shop!!!')

#boutta create my robot barista

name = input('What is your name?\n')
menu = 'black coffee, cappuccino, ice tea, milky tea, black tea.'
if name == 'ben' or name == 'loki':
    evil_status = input('are you evil?\n')
    good_deed = int(input('how many good deeds have you done today?\n'))
    if evil_status == 'yes' and good_deed <= 3:
     print('AAAHHH!! Get out Evil ' + name + ' your not welcome here!')
     exit()
    else:
        print('Oh, so you are one of the good ones. Well come on in!')
else:
    print('\n\nAlright ' + name + ', thank you for coming in today.Here is a list of what we are serving;\n\n'+menu)

   #was a bit tricky here ;-D

print('Here is a list of what we are serving;\n\n'+ menu +'\nwhat would you like to get from our menu today?')

order = input()

price = 5

if order == 'ice tea':
    price = 18
elif order == 'cappuccino':
    price = 5
    cream_status = input('do you want it with whipped cream?\n')
    if cream_status == "yes":
        price = 11
    else:
        price = 5

#this part had me thinking

elif order == 'milky tea':
    price = 12
elif order == 'black tea':
    price = 6
elif order == 'black coffee':
    price = 3
else:
    print('Sorry, we dont have that here.')
    exit()
amount = input('how many would you like to get?\n')

total = price * int(amount)

print('\nSounds good. We will have your order coming right up!')

print('Your total is $'+ str(total)+'.')



