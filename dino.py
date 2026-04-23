import pgzrun
import time
TITLE = "Dino Run"
WIDTH = 500
HEIGHT = 500
Score = 0 
bg = Actor("ground")
ob = Actor("obs")
d = Actor("dino")
ob2 = Actor("box")
d.pos = (50,295)
bg.pos = (250,250)
ob.pos = (250,320)
ob2.pos = (350,320)

def draw():
    global Score
    screen.fill(color="white")
    # screen.blit("ground",(0,250))
    bg.draw()
    d.draw()
    ob.draw()
    ob2.draw()
    screen.draw.text("Score: " + str(Score),color = "blue", topleft =(10,10))
def update():
    global Score
    """bg.x -= 2     
    if bg.right < 0:
        bg.left = WIDTH""" 
    ob.x-=2     
    if ob.right<0:
        ob.left = WIDTH
    ob2.x -= 2
    if ob2.right < 0:
         ob2.left = WIDTH 
    d.y+=4
    if d.y >= 295:
        d.y = 295
    if keyboard.space:
        d.y-=5
    if ob.x<90:     
        if d.colliderect(ob):
            Score -= 10
            
            ob.x=WIDTH
    if ob2.x<90:     
        if d.colliderect(ob2):
            Score -= 10
            
            ob2.x=WIDTH
pgzrun.go()
    
