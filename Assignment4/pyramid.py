"""
File: pyramid.py
----------------
ADD YOUR DESCRIPTION HERE
"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 9     # The number of bricks in the base

# Added Constants
BASE_WIDTH = BRICK_WIDTH * BRICKS_IN_BASE
NUMBER_OF_LAYERS = BRICKS_IN_BASE

def draw_pyramid(canvas):
    """
    ADD YOUR COMMENT
    """
    # Your code goes here


    start_location = CANVAS_WIDTH / 2 - BASE_WIDTH / 2
    layer_number = 1
    bricks_in_layer = BRICKS_IN_BASE

    for i in range(NUMBER_OF_LAYERS):
        build_a_layer(canvas, layer_number, bricks_in_layer, start_location)
        layer_number += 1
        bricks_in_layer -= 1
        start_location = CANVAS_WIDTH / 2 - (bricks_in_layer * BRICK_WIDTH) / 2



def build_a_layer(canvas, layer_number, bricks_in_layer, start_location):
    for i in range(bricks_in_layer):         # builds the base
        canvas.create_rectangle(start_location, CANVAS_HEIGHT - BRICK_HEIGHT * layer_number, start_location \
                                + BRICK_WIDTH, CANVAS_HEIGHT - BRICK_HEIGHT * (layer_number - 1))
        start_location += BRICK_WIDTH

def draw_centered_brick(canvas):
    x = (CANVAS_WIDTH - BRICK_WIDTH) / 2
    y = CANVAS_HEIGHT
    canvas.create_rectangle(x, y, x + BRICK_WIDTH, y - BRICK_HEIGHT)

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
