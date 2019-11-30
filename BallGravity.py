from turtle import*
up()
speed(0)
up()
hideturtle()
border = Turtle()

border.width(3)
border.speed(0)
border.hideturtle()
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)
border.up()
border.goto(70,0)
border.down()
border.goto(-70,0)

speedy = 0

def speedUp():
    global speedy
    speedy+=1

def speedDown():
    global speedy
    speedy-=1

def Zero():
    global x,y,speedy
    setpos(0,200)
    speedy = 0


shape('circle')
setpos(0, 200)
showturtle()

gravity = 0.1
x = 1
speedx = 1
while True:
    # x,y = round(x),round(y)
    speedy -= gravity
    # gravity += 0.001
    goto(xcor()+speedx, ycor()+speedy)
    # print(x,y)

    if ycor() <= -240:
        speedy = -speedy
        goto(xcor(),ycor()+speedy)

    if xcor() >= 240 or xcor() <= -240:
        speedx = -speedx
        # goto(x+speedx,y-speedy)
    if round(xcor()) in range(-80,80) and round(ycor()) in range (-10,10):
        speedy=-speedy
    #     goto(x+speedx,y-speedy)
    Screen().onkey(speedUp,'Up')
    Screen().onkey(Zero,'r')
    Screen().onkey(speedDown,'Down')
    Screen().listen()


exitonclick()
