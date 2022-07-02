import random


class Room:
    def __init__(self,
                 room_type: str = "",
                 directions: str = "",
                 haunted: int = random.randint(0, 3)
                 ):
        self.room_type: str = room_type
        self.directions: str = directions
        self.haunted: int = haunted

        if self.haunted == 3:
            self.haunted = True
        else:
            self.haunted = False


def main():
    lives = 3
    dead = False

    while not dead:
        pass


main()
