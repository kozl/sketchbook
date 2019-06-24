WIDTH=720
HEIGHT=1080
SQUARE_SIZE=4
WIDTH_SQUARES=ceil(float(WIDTH)/SQUARE_SIZE)
HEIGHT_SQUARES=ceil(float(HEIGHT)/SQUARE_SIZE)

def setup():
    frameRate(5)
    size(WIDTH,HEIGHT)
    
def draw():
    draw_squares(SQUARE_SIZE, fill_with_random)

def draw_squares(square_size, get_color_func):
    x = 0
    y = 0
    noStroke()
    for wdth in range(HEIGHT_SQUARES):
        for hght in range(WIDTH_SQUARES):
            r, g, b = get_color_func(wdth, hght)
            fill(r, g, b)
            rect(x, y, square_size, square_size)
            x+=square_size
        x=0
        y+=square_size
            
            
def fill_with_random_grayscale(wdth, hght):
    color = int(random(255))
    return color, color, color

def fill_with_random_grayscale2(wdth, hght):
    color = int(random((255/WIDTH_SQUARES*0.5)*wdth, 255))
    return color, color, color

def fill_with_random(wdth, hght):
    r = int(random(255))
    g = int(random(255))
    b = int(random(255))
    return r, g, b
