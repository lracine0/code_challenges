

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


def add_shapes(canvas, start_x, start_y, end_x, end_y, fill_char):
    """Add rectangle to canvas with coordinates set 1 and 2,
       set 1: top left corner, set 2: bottom right corner"""
 

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            canvas[i][j] = fill_char

    if canvas[0][0] == 0:

        for i in range(10):
            for j in range(10):
                if canvas[i][j] != fill_char:
                    canvas[i][j] = "-"


    print_canvas(canvas)
    bool_add_more = input("Would you like to add another shape? y/n  ")

    if bool_add_more == "y":
        coords = input("Give new coordinates for shape with fill character  ")
        list_coords = list(coords)
        start_x = coords[0]
        start_y = coords[1]
        end_x = coords[2]
        end_y = coords[3]
        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)
        fill_char = coords[4]
        add_shapes(canvas, start_x, start_y, end_x, end_y, fill_char)

    else:
        print("Thanks, bye!")



def print_canvas(canvas):
    """Prints canvas row by row"""


    for i in range(10):
        print(canvas[i])


canvas = default_canvas()
add_shapes(canvas, 3, 3, 7, 7, "?")












