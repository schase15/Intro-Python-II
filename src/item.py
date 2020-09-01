# Create Item class
# Create subclasses later for specialized items (like weapons)

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"({self.name}: {self.description})"
