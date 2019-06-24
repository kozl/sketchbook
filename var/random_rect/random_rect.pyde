WIDTH=720
HEIGHT=1080
t=0.0

def setup():
    frameRate(1000)
    background(0)
    fullScreen()
    # size(WIDTH,HEIGHT)
    
def draw():
    global t
    translate(width/2, height/2)
    rotate(t)
    strokeWeight(5)
    rect(random(100, width), random(100, height), random(200), random(100))
    t+=0.5
    
def x(t):
    return t*2

def y(t):
    return sin(t/5)*100
