# Create a text adventure game using interaction with the terminal

# Imports from other pages
from room import Room
from player import Player
from item import Item

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


# Create some items to put in rooms, store in dictionary

items = {
    'torch': Item("torch", "Hand-held flickering flame"),
    'shovel': Item("shovel", "Rusty shovel with a broken handle")
}

# Add items to rooms:

room['Outside Cave Entrance'].room_items = items['torch']
room['Foyer'].room_items = items['shovel']



### Main Game ###

# Get users input for their name, use that name to create a player that is located outside the cave
print("--------------------------")
user_name = input("Welcome to The Game! What is your name? \n")

# Create instance of player using the users name. Starting point is outside the cave.
player1 = Player(name= user_name, current_room= room['Outside Cave Entrance'])

# Print a welcome message to the player, explaining game.
print("--------------------------")
print(f"(Welcome {player1.name}! You find yourself standing at the entrance to a large cave. Please use the cardinal directions to navigate through the cave in search of the buried treasure!)\n")
print("--------------------------")


# Write a continuous game loop:
while True:

    # Print the current name and description of where the player is located
    print(f"(You are currently located {player1.current_room}.)\n")
    print("--------------------------")

    # If the room has items, if statement telling the player the items and asking if the player wants to add items
    if hasattr(player1.current_room, 'room_items'):

        # Print out items in the room
        print(f"(This room appears to contain a {player1.current_room.room_items})\n")

        # Ask if the user would like to pick up any items
        pickup_yes_no = input("Would you like to pick up any of these items? [yes] [no] ")

        # If yes, have the player use the pickup method, if no continue on with the game
        if pickup_yes_no == 'yes':

            # Set it so that the user can only carry one item at a time 
            # Expand this later, limited by the basic layout of the game

            # If the user already has an item, ask them if they would like to drop it
            if len(player1.inventory) > 0:
                print(f"(You can only carry 1 item at a time)\n")
                drop_yes_no = input(f"(Would you like to drop {player1.inventory[0].name} from your inventory? [yes] [no])")

                # If the user wants to drop their current item
                if drop_yes_no == 'yes':

                    # Have the user drop their item
                    item = player1.inventory[0]
                    player1.drop(item)
                    print(f"(Dropped {item})\n")

                    # After droping their item, the user can now pick up a new item
                    pickup_item = input('Which item would you like to pickup? ')
                    player1.pickup(items[pickup_item])
                    print(f"(You have picked up {items[pickup_item]}. It can now be found in your inventory)\n")
                    print(f"Your current inventory includes: \n {player1.inventory}\n")

                # If they don't want to drop their item continue on with the game
                else:
                    print("Keeping current item")

            # If the user doesn't already have an item
            else:
                pickup_item = input('Which item would you like to pickup? ')

                # Pickup the item
                player1.pickup(items[pickup_item])
                print(f"(You have picked up {items[pickup_item]}. It can now be found in your inventory)\n")

                # Show them their inventory
                print(f"Your current inventory includes: \n {player1.inventory}\n")
        
        # If they do not want the new item
        else:
            print("Leaving items behind")

    # If room is empty
    else:
        print("This room seems empty...")

    # Takes direction input from user to guide player
    direction = input('Which direction would you like to move?: ')
    print("--------------------------")


    # Clean input of upper and lower case, of multiple words
    # Take just the first word in the list
    direction = direction.strip().lower().split()[0]
    # Take only the first character of the clean word (n, s, e, w)
    direction = direction[0]

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
        print("That's not a direction! Select North, East, South or West. Or type quit to leave the game.")
        print("--------------------------")
        continue

