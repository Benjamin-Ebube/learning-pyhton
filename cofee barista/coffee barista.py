print('Hello friend, welcome to my coffee shop!!!')

#boutta create my robot barista

name = input('What is your name?\n').lower()
menu = 'black coffee, cappuccino, ice tea, milky tea, black tea.'
if name == 'ben' or name == 'loki':
    evil_status = input('are you evil?\n').lower()
    good_deed = int(input('how many good deeds have you done today?\n'))
    if evil_status == 'yes' and good_deed <= 3:
     print('AAAHHH!! Get out Evil ' + name + ' your not welcome here!')
     exit()
    else:
        print('Oh, so you are one of the good ones. Well come on in!')
else:
    print('\n\nAlright ' + name + ', thank you for coming in today.')

   #was a bit tricky here ;-D

print('What would you like to get from our menu today? Here is a list of what we are serving;\n\n'+menu)
order = input()
servings=('black coffee', 'cappuccino', 'ice tea', 'milky tea', 'black tea')
a,b,c,d,e = servings

#for option in servings:
    #   if order
#order_counter = 0
#while order_counter < 4:
#    if order != [a, b, c, d, e]:
#        input("sorry we don't have that here. Why dont you try something else that we have in our menu;\n" + menu)
#    break
#order_counter += 1

price = 5

if order == a:
    price = 18
elif order == b:
    price = 5
    cream_status = input('do you want it with whipped cream?\n')
    if cream_status == "yes":
        price = 11
    else:
        price = 5

#this part had me thinking

elif order == c:
    price = 12
elif order == d:
    price = 6
elif order == e:
    price = 3
else:
    print('sorry we dont have that here.')
    exit()

amount = input('how many would you like to get?\n')

total = price * int(amount)

print('\nSounds good. We will have your order coming right up!')

print('Your total is $'+ str(total)+'.')

