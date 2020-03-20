#You'll be in charge of implementing the API for drawing rectangles (and squares). The API must be able to:

#Render canvas
#Print the canvas and any shapes to standard output
#Add a shape to a canvas
#shape the shape to add. For now, assume you only have to deal with rectangles
#Clear all shapes from a canvas
#Create a rectangle
#start_x is the X coordinate of the upper-left-hand corner of the rectangle
#start_y is the Y coordinate of the upper-left-hand corner of the rectangle
#end_x is the X coordinate of the lower-right-hand corner of the rectangle
#end_y is the Y coordinate of the lower-right-hand corner of the rectangle
#fill_char is the character that should be used to draw the rectangle
#Change a rectangle's fill character
#char the character to use in order to draw a pre-existing rectangle
#Translate (move left, right, up, or down)
#axis which axis ('x' or 'y') should we translate the rectangle on? Translating on the X-axis will cause the rectangle to move left and right. 
#Translating on the Y-axis will cause the rectangle to move up and down.
#num is how much to move the rectangle. Negative numbers will cause the rectangle to shift left or down. 
#Positive numbers will cause the rectangle to #shift right or up.
#For now, assume that you're always working with a 10-by-10 character canvas (that's 10 characters wide and 10 characters tall). 
#Although it would be nice to implement an API for users to specify the dimensions 
#of their canvas, assume that another developer will be responsible for that.


# Pseudo code:
# 10x10 canvas shape 
# given two (x, y) coordinates for top left and bottom right corner
# fill char

def default_canvas():
    """Returns default canvas"""


    canvas = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

    return canvas


def add_shapes(start_x, start_y, end_x, end_y, fill_char):
    """Add rectangle to canvas with coordinates set 1 and 2,
       set 1: top left corner, set 2: bottom right corner"""


    canvas = default_canvas()

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            canvas[i][j] = fill_char

    for i in range(10):
        for j in range(10):
            if canvas[i][j] != fill_char:
                canvas[i][j] = "-"

    print_canvas(canvas)


def print_canvas(canvas):
    """Prints canvas row by row"""


    for i in range(10):
        print(canvas[i])


add_shapes(3, 3, 7, 7, "?")













