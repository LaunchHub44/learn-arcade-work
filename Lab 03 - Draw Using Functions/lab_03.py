import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Lab 2 Drawing')
arcade.set_background_color((5, 20, 50))


def draw_ground():
    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8, SCREEN_WIDTH, SCREEN_HEIGHT / 2,
                                 arcade.csscolor.WHITE)


def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 25, 75, (200, 150, 100))
    arcade.draw_triangle_filled(
        x + 50, y + 25,
        x - 50, y + 25,
        x, y + 125,
        (75, 100, 75)
    )

    arcade.draw_triangle_filled(
        x + 50, y + 75,
        x - 50, y + 75,
        x, y + 175,
        (75, 100, 75)
    )

    arcade.draw_triangle_filled(
        x + 40, y + 100,
        x - 40, y + 100,
        x, y + 175,
        arcade.csscolor.WHITE
    )


def main():
    arcade.start_render()
    draw_ground()
    draw_tree(100, 260)
    draw_tree(245, 260)
    draw_tree(385, 260)
    draw_tree(525, 260)
    arcade.finish_render()
    arcade.run()


main()
