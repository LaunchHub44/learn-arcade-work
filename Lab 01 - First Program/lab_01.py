# Lab 1
#  https://www.youtube.com/watch?v=wYofTQaIIlQ

import arcade

arcade.open_window(600, 600, 'First Window')

arcade.set_background_color(arcade.csscolor.SIENNA)
arcade.start_render()
arcade.draw_rectangle_filled(300, 300, 25, 25, arcade.csscolor.AZURE)
arcade.finish_render()

arcade.run()