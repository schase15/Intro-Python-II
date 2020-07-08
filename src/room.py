# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to= "Error", s_to= "Error", e_to= "Error", w_to= "Error"):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __repr__(self):
        return f"(Name: {self.name}\n Description: {self.description})"

    