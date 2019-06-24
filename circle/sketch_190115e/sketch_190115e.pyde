def setup():
    size(600, 600)
    background(0)
    noStroke()
    translate(width/2, height/2)
    fill(255)
    rect(-100, -100, 200, 200)

def draw():
    for i in range(10):
        angle = map(i, 0, 50, 0, 360)
        gray = map(i, 0, 50, 0, 255)
        pushMatrix()
        translate(width/2, height/2)
        rotate(angle)
        fill(gray)
        rect(-100, -100, 200, 200)
        popMatrix()
    # for i in reversed(range(7)):
    #     sz = map(i, 0, 7, 0, 230)
    #     gray = map(i, 0, 7, 0, 255)
    #     pushMatrix()
    #     translate(width/2, height/2)
    #     rotate(angle)
    #     fill(gray)
    #     ellipse(0, 0, sz, sz)
    #     popMatrix()
    fill(255)
