# Arcade module
import arcade

# Window
arcade.open_window(500, 500, 'Lab 2 Drawing')
arcade.set_background_color((5, 20, 50))

# Rendering
arcade.start_render()

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
arcade.finish_render()

arcade.run()