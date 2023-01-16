# exercise GUI

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# 1 iterate
    # if 0 -> print '1'
    # if 1 -> print '*'

fill = '*'
empty = ' '

def print_pixel(pixel):
    pixel_value = fill if pixel else empty
    print(pixel_value, end = '')

def new_line():
    print('')
    
def print_picture(picture):
    for row in picture:
        for pixel in row:
            print_pixel(pixel)
        new_line()

print_picture(picture)
