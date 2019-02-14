import arcade

#Function for dynamic tree creation, off seting points based on the bottom-left point of rectangle
def draw_tree(x,y):
    arcade.draw_xywh_rectangle_filled(x,y,20,95, arcade.color.BROWN)
    arcade.draw_triangle_filled(x-30, y+75, x+50, y+75, x+10, y+150,arcade.color.GREEN)

WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
# Begin drawing

arcade.draw_xywh_rectangle_filled(0, 0,640, 100,  arcade.color.APPLE_GREEN)

#Drawing 3 trees and a sun
arcade.draw_circle_filled(WIDTH-100, HEIGHT-100, 50, arcade.color.YELLOW)
draw_tree(200,50)
draw_tree(WIDTH-200,50)
draw_tree(WIDTH-125,50)

# End drawing
arcade.finish_render()
arcade.run()
