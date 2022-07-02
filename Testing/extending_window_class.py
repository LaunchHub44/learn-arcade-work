import arcade

class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

def main():
    run_game = Game(640, 480, "Game")

    arcade.run()

main()