help = "start - to start the car\nstop - to stop the car\nquit - to exit the game"
start = 'your car has started!'
stop = 'your car has stopped'
print('welcome')
started = False
while True:
    response = input('> ').lower()

    if response == 'start':
        if started :
            print('car is already started')
        else:
            started = True
            print('your car has started')
    elif response == 'help':
       print(help)
    elif response == 'stop':
        if not started:
            print('your car is already stopped')
        else:
            started = False
            print(stop)
    elif response == 'quit':
        exit()
    else:
     print('Sorry i dont understand that. Try "help" for the instruction manual.')
