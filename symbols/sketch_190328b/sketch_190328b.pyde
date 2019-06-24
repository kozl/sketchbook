import random
from itertools import chain

PIXELS = 5
SYMBOL_WIDTH = 10
SYMBOL_HEIGHT = 10
SYMBOL_SIZE = 50
SYMBOL_BLANK = 15
WIDTH = SYMBOL_SIZE * SYMBOL_WIDTH + (SYMBOL_WIDTH + 1)*SYMBOL_BLANK
HEIGHT = SYMBOL_SIZE * SYMBOL_HEIGHT + (SYMBOL_HEIGHT + 1)*SYMBOL_BLANK
RANDOM_PIXELS = 8

BLANK = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],]


class Symbol:
    def __init__(self, x, y, sz):
        self._matrix = [[None]*PIXELS for i in range(PIXELS)]
        self._rand_coords = [(x, y) for x in range(PIXELS) for y in range(PIXELS)]
        random.shuffle(self._rand_coords)
        
        pixel_size = sz / PIXELS
        pixel_x = x
        pixel_y = y
        for i in range(PIXELS):
            for k in range(PIXELS):
                self._matrix[i][k] = Pixel(pixel_x, pixel_y, pixel_size)
                pixel_x += pixel_size
            pixel_x = x
            pixel_y += pixel_size

    def letter(self, layout):
        for px in range(PIXELS):
            for py in range(PIXELS):
                if layout[px][py] == 1:
                    self._matrix[px][py].maxcount = 2
                else:
                    self._matrix[px][py].maxcount = 10000

    def activated_pixels(self):
        activated = 0
        for pixel in chain.from_iterable(zip(*self._matrix)):
            if pixel.activated:
                activated += 1
        return activated

    def get_n_random(self, n):
        rand_coords = random.sample(self._rand_coords, n)
        return [self._matrix[x][y] for x, y in rand_coords]

    def update(self):
        black_pixels = RANDOM_PIXELS - self.activated_pixels()
        for pixel in self.get_n_random(black_pixels):
            if not pixel.activated:
                pixel.color = (0, 0, 0)
                pixel.hitcount += 1
                if pixel.hitcount > pixel.maxcount:
                    pixel.activated = True
            else:
                new_pixel = self.get_n_random(1)[0]
                if not new_pixel.activated:
                    new_pixel.color = (0, 0, 0)
        for pixel in chain.from_iterable(zip(*self._matrix)):
            if pixel.activated:
                pixel.color = (255, 0, 0)

    def draw(self):
        for pixel in chain.from_iterable(zip(*self._matrix)):
                pixel.draw()
        
class Pixel:
    def __init__(self, x, y, sz, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.sz = sz
        self.color = color
        self.activated = False
        self.maxcount = 0
        self.hitcount = 0

    def activate(self):
        self.activated = True

    def draw(self):
        fill(*self.color)
        noStroke()
        rect(self.x, self.y, self.sz, self.sz)
        self.color = (255, 255, 255)


def setup():
    global matrix
    size(WIDTH, HEIGHT)
    symbol_x, symbol_y = SYMBOL_BLANK, SYMBOL_BLANK
    matrix = [[None]*SYMBOL_WIDTH for i in range(SYMBOL_HEIGHT)]
    for i in range(SYMBOL_HEIGHT):
        for k in range(SYMBOL_WIDTH):
            s = Symbol(symbol_x, symbol_y, SYMBOL_SIZE)
            s.letter(BLANK)
            matrix[i][k] = s
            symbol_x += SYMBOL_BLANK + SYMBOL_SIZE
        symbol_x = SYMBOL_BLANK
        symbol_y += SYMBOL_BLANK + SYMBOL_SIZE
    
def draw():
    global matrix
    if frameCount % 15 == 0:
        background(255)
        x = 0
        for symbol in chain.from_iterable(zip(*matrix)):
            symbol.update()
            symbol.draw()
            
            print(symbol._matrix[0][0].x)
