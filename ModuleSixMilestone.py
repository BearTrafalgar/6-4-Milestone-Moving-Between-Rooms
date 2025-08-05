#Alexander Stanley
#IT-140
#8-3-25

rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}
#dict assigning adjacent rooms and allowed directions

current_room = 'Great Hall'
#Starting player in the 'Great Hall'

while current_room != 'Cellar':
    #Entering the cellar is a gameplay loop exit, while loop to keep game going aslong as not in cellar

    print('You are in the {}.'.format(current_room))
    print(f'What direction would you like to go? {" or ".join(rooms.get(current_room, {}).keys())}')
    #Informaing player of current room and possible directions to go

    user_inp = input().title()
    #Formatting user input to have first letter capitalized to match dict formatting

    if user_inp == 'Exit' or 'Quit':
        quit()
    #Gameplay loop exit, entering exit or quit will terminate the game

    if user_inp not in rooms.get(current_room, {}):
        print('There is a wall there silly! Try a different direction.')
        continue
    #If player enters a direction not available in current room an error will be displayed informing them


    current_room = rooms.get(current_room).get(user_inp)
    #Setting current_room to new room in corresponding dict value based on input

    if current_room == 'Cellar':
        print('You found a secret tunnel to freedom!')
    #Gameplay loop exit, if player enters the cellar, gameplay is terminated