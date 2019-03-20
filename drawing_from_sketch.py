import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass

def draw_tree(x,y,w,h,factor):
	arcade.xywhrectangle(x,y,w,h,(0,0,0))
	arcade.triangle(x-factor,y+h,x+w+factor,x+w/2,y+h+factor)

def on_draw():
    arcade.start_render()
    # Draw in here...
    for numb in range(0,5):
	draw_trees(numb**2,20,30,50,25)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
