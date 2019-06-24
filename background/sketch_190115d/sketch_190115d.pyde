MAX_FIGURES = 5
MAX_SQUARES = 5

def setup():
    size(720, 1080)
    noStroke()
    background(0)
    
def draw():
    for fig in range(int(random(MAX_FIGURES))):
        draw_fig(random(width),random(height), random(20), int(random(MAX_SQUARES)))

        
def draw_fig(x, y, w, squares):
    for square in range(0, squares):
        gray = map(square, 0, squares, 0, 255)
        fill(gray)
        rect(x+square*5, y+square*5, w, w)
