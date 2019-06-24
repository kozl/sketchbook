import random

PIXELS = 5
SYMBOL_WIDTH = 10
SYMBOL_HEIGHT = 10
SYMBOL_SIZE = 30
SYMBOL_BLANK = 15
WIDTH = SYMBOL_SIZE * SYMBOL_WIDTH + (SYMBOL_WIDTH + 1)*SYMBOL_BLANK
HEIGHT = SYMBOL_SIZE * SYMBOL_HEIGHT + (SYMBOL_HEIGHT + 1)*SYMBOL_BLANK

class Symbol:
    def __init__(self, x, y, sz, letter=None):
        self.matrix = [[None]*PIXELS for i in range(PIXELS)]
        
        pixel_size = sz / PIXELS
        pixel_x = x
        pixel_y = y
        for i in range(PIXELS):
            for k in range(PIXELS):
                self.matrix[i][k] = Pixel(pixel_x, pixel_y, pixel_size)
                pixel_x += pixel_size
            pixel_x = x
            pixel_y += pixel_size
        
        self.random_pixels = 8
        if letter:
            self.random_pixels = letter.len()
    
    def get_glowing(self):
        glowing = []
        for i in range(PIXELS):
            for k in range(PIXELS):
                if self.matrix[i][k].glow:
                    glowing.append((i, k))
        return glowing
    
    
    def get_n_random(n):
        coord = [(x, y) for x in range(PIXELS) for y in range(PIXELS)]
        return random.sample(coord, n)
    
    def update(self):
        total = self.get_glowing() + self.get_n_random(self.random_pixels - len(glowing))
        for i, k in range(glowing):
            self.matrix[i][k].update()
        
        for i, k in range():
            self.matrix[i][k].update()
    
    def draw(self):
        for i in range(PIXELS):
            for k in range(PIXELS):
                if self.matrix[i][k].glow:
                    self.matrix[i][k].update()
                self.matrix[i][k].draw()
        
class Pixel:
    def __init__(self, x, y, sz, color=255):
        self.x = x
        self.y = y
        self.sz = sz
        self.color = color
        self.glow = False
    
    def update(self):
        if self.glow:
            self.color = (255, 0, 0)
        else:
            self.color = 0
    
    def draw(self):
        fill(self.color)
        noStroke()
        rect(self.x, self.y, self.sz, self.sz)
        self.color = 255

symbol_x, symbol_y = SYMBOL_BLANK, SYMBOL_BLANK
matrix = [[None]*SYMBOL_WIDTH for i in range(SYMBOL_HEIGHT)]
for i in range(SYMBOL_HEIGHT):
    for k in range(SYMBOL_WIDTH):
        matrix[i][k] = Symbol(symbol_x, symbol_y, SYMBOL_SIZE)
        symbol_x += SYMBOL_BLANK + SYMBOL_SIZE
    symbol_x = SYMBOL_BLANK
    symbol_y += SYMBOL_BLANK + SYMBOL_SIZE


def setup():
    size(WIDTH, HEIGHT)
    background(0)
    
def draw():
    if frameCount % 15 == 0:
        background(255)
        for i in range(SYMBOL_HEIGHT):
            for k in range(SYMBOL_WIDTH):
                matrix[i][k].update()
                matrix[i][k].draw()
