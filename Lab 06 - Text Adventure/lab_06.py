import random

#
# ADVANCED Topic:
#
# You are welcome to use either of "case 1" or "case 2"
#
# case 2 is preferred.
#  In industry, fewer variables are better!
#

class Room:
    def __init__(self,
                 room_type: str = "",
                 directions: str = "",
                 ghost_chance: int = random.randint(0,3)
                 ):
        self.room_type: str = room_type
        self.directions: str = directions
        self.ghost_chance: int = ghost_chance

        # case 1
        self.is_haunted_var = False
        if ghost_chance >= 3:
            self.is_haunted_var = True

    # case 2  (in industry practice, this is preferred. )
    def is_haunted(self) -> bool:
        return self.ghost_chance >= 3


def main():
    lives = 3
    dead = False

    r = Room()
    if r.is_haunted_var:
        # We maintain state in a state variable:  is_haunted_var
        pass

    # OR,
    if r.is_haunted():
        # We calculate haunted status, everytime we check.
        pass


    while not dead:
        pass


main()
