import pgzrun
import random
WIDTH=700
HEIGHT=600
Bob=Actor("cat3")
Bob.x=300
Bob.y=235
msg="Click on Cat"
counter=0
def draw():
    screen.fill("White")
    Bob.draw()
    screen.draw.text(msg,(350,100),color="Black")
    screen.draw.text(str(counter),(50,50),color="Black")
def update():
    pass
def on_mouse_down(pos):
    global msg,counter
    if Bob.collidepoint(pos):
        Bob.x=random.randint(50,WIDTH-50)
        Bob.y=random.randint(50,HEIGHT-50)
        msg="Enjoy clicking!"
        counter+=1
    else:
        msg="Oops! Not the Cat!"
pgzrun.go()