# Arcade module
import arcade

# Window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Lab 2 Drawing')
arcade.set_background_color((5, 20, 50))


def draw_boat(x, y):
    arcade.draw_arc_filled(x, y, 150, 100, (100, 50, 25), 180, 360)
    arcade.draw_rectangle_filled(x, y + 37, 10, 75, (100, 100, 100))
    arcade.draw_polygon_filled(
        [(x + 5, y + 25),
         (x + 50, y + 25),
         (x + 5, y + 75)],
        (200, 200, 200)
    )


def draw_fish(x, y, color):
    arcade.draw_ellipse_filled(x, y, 50, 35, color)
    arcade.draw_triangle_filled(
        x - 25, y,
        x - 45, y - 25,
        x - 45, y + 25,
        color
    )


# Rendering
arcade.start_render()


def background():
    arcade.draw_circle_filled(250, 220, 100, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(250, 100, 500, 250, (0, 50, 50))
    arcade.draw_polygon_filled(
        [(150, 225),
         (100, 0),
         (400, 0),
         (350, 225)],
        (200, 255, 255)
    )
    arcade.draw_arc_filled(250, 225, 200, 200, (200, 225, 255), 180, 360)


# For Testing
background()
draw_boat(250, 250)
draw_fish(100, 100, (100, 0, 0))
draw_fish(200, 50, (0, 100, 0))

arcade.finish_render()

arcade.run()
