import pgzrun

TITLE = "Dino Run"
WIDTH = 500
HEIGHT = 500

bg = Actor("ground")
ob = Actor("obs")
d = Actor("dino")
d.pos = (50,295)
bg.pos = (250,250)
ob.pos = (250,281)
def draw():
    screen.fill(color = "white")
    bg.draw()
    d.draw()
    ob.draw()
def update():
    bg.x -= 2     
    if bg.right < 0:
        bg.left = WIDTH 
pgzrun.go()
