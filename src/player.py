# Write a class to hold player information, e.g. what room they are in currently.
# Blank inventory list to be added to as the player moves through the game


class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    
    def __repr__(self):
        return f"(Name: {self.name}\n Current location: {self.current_room})"

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)
    