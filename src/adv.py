# Create a text adventure game using interaction with the terminal

    # Plan:
    '''
    The user will input a name which creates a player
    '''


from room import Room
from player import Player

# Declare all the rooms
    # I changed the keys of the dictionary to match the names of the Room object so that I could 
    # use player1.current_room.name to reference the dictionary directly

room = {
    'Outside Cave Entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'Foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'Grand Overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'Narrow Passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'Treasure Chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
    # Populate the blank parameters on the Room objects
    # The default direction parameters is 'Error', so if there is not a route to overwrite it, it will return 'Error'

room['Outside Cave Entrance'].n_to = room['Foyer']
room['Foyer'].s_to = room['Outside Cave Entrance']
room['Foyer'].n_to = room['Grand Overlook']
room['Foyer'].e_to = room['Narrow Passage']
room['Grand Overlook'].s_to = room['Foyer']
room['Narrow Passage'].w_to = room['Foyer']
room['Narrow Passage'].n_to = room['Treasure Chamber']
room['Treasure Chamber'].s_to = room['Narrow Passage']


# Main

# Get users input for their name, use that name to create a player that is located outside the cave
print("--------------------------")
user_name = input("Welcome to The Game! What is your name? \n")

# Create instance of player using the users name. Starting point is outside the cave.
player1 = Player(name= user_name, current_room= room['Outside Cave Entrance'])

# Print a welcome message to the player, explaining game.
print("--------------------------")
print(f"(Welcome {player1.name}! You find yourself standing at the entrance to a large cave. Please use the cardinal directions [n, e, s, w] to navigate through the cave in search of the buried treasure!)\n")
print("--------------------------")

# Take user input for direction
    # If statements: if user selects n -> look at n_to. If it is "Error" print error message. 
    # Otherwise update player1.current_room to new room
    # Need to link current room in player class to its matched room in room class


# Write a continuous game loop:
while True:

    # Print the current name and description of where the player is located
    print(f"(You are currently located {player1.current_room}.)\n")
    print("--------------------------")

    # Takes direction input from user to guide player
    direction = input('Which direction would you like to move? [n, e, s,w]: ')
    print("--------------------------")

    # Move player from their current room to the south 
    if direction == "n":
        if room[player1.current_room.name].n_to == "Error":
            print('You have hit a wall! Try again')
            print("--------------------------")
        else:
            player1.current_room = room[player1.current_room.name].n_to
            print("You have moved North")
            print("--------------------------")

    # Move player from their current room to the East
    elif direction == "e":
        if room[player1.current_room.name].e_to == "Error":
            print('You have hit a wall! Try again')
            print("--------------------------")
        else:
            player1.current_room = room[player1.current_room.name].e_to
            print("You have moved East")
            print("--------------------------")

    # Move player from their current room to the south 
    elif direction == "s":
        if room[player1.current_room.name].s_to == "Error":
            print('You have hit a wall! Try again')
            print("--------------------------")
        else:
            player1.current_room = room[player1.current_room.name].s_to
            print("You have moved South")
            print("--------------------------")

    # Move player from their current room to the west
    elif direction == "w":
        if room[player1.current_room.name].w_to == "Error":
            print('You have hit a wall! Try again')
            print("--------------------------")
        else:
            player1.current_room = room[player1.current_room.name].w_to
            print("You have moved West")
            print("--------------------------")

    # Allow the user to exit the game
    elif direction == "q":
        print("Thank you for playing The Game! You are now leaving.")
        print("--------------------------")
        break

    # Catch all response in case anything other than n, s, e, w, or quit is input
    else:
        print("That's not a direction! Select n for North, e for East, s for South, w for West. Or type 'q' to quit the game.")
        print("--------------------------")
        continue

