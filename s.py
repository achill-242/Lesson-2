import pgzrun
import random
WIDTH = 500
HEIGHT = 500


star = Actor("star")
star.pos = (250, 250)

import random
dx = random.choice([-3, 3])
dy = random.choice([-3, 3])

def draw():
    screen.blit("space", (0, 0)) 
    star.draw()

def update():
    global dx, dy

    
    star.x += dx
    star.y += dy

    
    if star.left <= 0 or star.right >= WIDTH:
        dx = -dx

    if star.top <= 0 or star.bottom >= HEIGHT:
        dy = -dy
pgzrun.go()