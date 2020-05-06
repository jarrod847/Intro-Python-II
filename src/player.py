# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def north(self):
        if self.location.n_to != None:
            self.location = self.location.n_to
        else:
            print("Can't travel North from this room, try another direction")

    def east(self):
        if self.location.e_to != None:
            self.location = self.location.e_to
        else:
            print("Can't travel East from this room, try another direction")

    def south(self):
        if self.location.s_to != None:
            self.location = self.location.s_to
        else:
            print("Can't travel South from this room, try another direction")

    def west(self):
        if self.location.w_to != None:
            self.location = self.location.w_to
        else:
            print("Can't travel West from this room, try another direction")
