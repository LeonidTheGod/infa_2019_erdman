from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()

"""
need - Сделать код читабельным и документированным.
need - Реализовать подсчёт очков.
need - Сделать шарики двигающимися со случайным отражением от стен.
need - Реализовать одновременное присутствие нескольких шариков на экране.
need - Добавить второй тип мишени со своей формой и своим специфическим харктером движения.
need - Выдавать за эти мишени другое количество очков.
need - Сделать таблицу лучших игроков, авматически сохраняющуюся в файл.
"""

colors = ['red','orange','yellow','green','blue']
root_x, root_y = 1000, 600
ball_cought = 0
count_width, count_height = 60, 50
canv_width, canv_height = 800, 500
root_geom = str(root_x) + 'x' + str(root_y)
root.geometry(root_geom)
canv = Canvas(root, width= canv_width, height = canv_height,bg='ivory')
count = Canvas(root, width= count_width, height = count_height ,bg='skyblue')
canv.pack()
count.pack(side = LEFT)
speedx =rnd(2, 6)
speedy =rnd(2, 6)
speedx1 =rnd(2, 6)
speedy1 =rnd(2, 6)
speedx2 = rnd(2, 6)
speedy2 =rnd(2, 6)
speedx3 = choice([-9, -6, -7, -8, 8, 7, 6, 9, 0])
speedy3= choice([-9, -6, -7, -8, 8, 7, 6, 9, 0])


balls = []
def new_ball():
    global x, y, r, ball
    r = rnd(10,50)
    x = rnd((root_x - canv_width) / 2 - r, (root_x - canv_width) / 2 + canv_width - r * 4 - 10 )
    y = rnd(50,450)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors)) 
    balls.append([x, y]) 
    print(ball)

def new_ball1():
    global x1, y1, r1, ball1
    r1 = rnd(10,50)
    x1 = rnd((root_x - canv_width) / 2 - r1, (root_x - canv_width) / 2 + canv_width - r1 * 4 - 10 )
    y1 = rnd(50,450)
    ball1 = canv.create_oval(x1 -r1 ,y1 -r1 ,x1 +r1 ,y1 +r1 ,fill = choice(colors))   
    balls.append([x1, y1]) 
    print(balls)


def new_ball2():
    global x2, y2, r2, ball2
    r2 = rnd(10,50)
    x2 = rnd((root_x - canv_width) / 2 - r2, (root_x - canv_width) / 2 + canv_width - r2 * 4 - 10 )
    y2 = rnd(50,450)
    ball2 = canv.create_oval(x2 -r2 ,y2 -r2 ,x2 +r2 ,y2 +r2 ,fill = choice(colors)) 
    balls.append([x2, y2]) 
    print(balls)

def new_ball3():
    global x3, y3, r3, ball3
    r3 = rnd(10,30)
    x3 = rnd((root_x - canv_width) / 2 - r3, (root_x - canv_width) / 2 + canv_width - r3 * 4 - 10 )
    y3 = rnd(50,450)
    ball3 = canv.create_rectangle(x3 -r3 ,y3 -r3 ,x3 +r3 ,y3 +r3 ,fill = choice(colors))    


def ball_motion():
    global balls
    # print(balls)
    global speedx, speedy, x, y, r
    global speedx1, speedy1, x1, y1, r1
    global speedx2, speedy2, x2, y2, r2
    global speedx3, speedy3, x3, y3, r3

    canv.move(ball, speedx, speedy)
    canv.move(ball1, speedx1, speedy1)
    canv.move(ball2, speedx2, speedy2)
    canv.move(ball3, speedx3, speedy3)

    root.after(10,ball_motion)

    # balls[0][0] += speedx
    # balls[0][1] += speedy  
    # balls[1][0] += speedx1
    # balls[1][1] += speedy1  
    # balls[2][0] += speedx2
    # balls[2][1] += speedy2    
    # x3 += speedx3
    # y3 += speedy3

    if canv.coords(ball)[2] >= canv_width or canv.coords(ball)[2] <= 0 + 2 * r:
        speedx = -speedx
        speedy = round(speedy / abs(speedy)) * rnd(2, 6)
    if canv.coords(ball1)[2] >= canv_width  or canv.coords(ball1)[2] <= 0 + 2 * r1:
        speedx1 = -speedx1
        speedy1 = round(speedy1 / abs(speedy1)) * rnd(2, 6)
    if canv.coords(ball2)[2] >= canv_width  or canv.coords(ball2)[2] <= 0 + 2 * r2:
        speedx2 = -speedx2
        speedy2 = round(speedy2 / abs(speedy2)) * rnd(2, 6)    
    if canv.coords(ball3)[2] >= canv_width  or canv.coords(ball3)[2] <= 0:
        speedx3 = -speedx3
        speedy3 = choice([-9, -6, -7, -8, 8, 7, 6, 9, 0])

    if canv.coords(ball)[3] >= canv_height or canv.coords(ball)[3] <= 0 + 2 * r:
        speedy = -speedy
        speedx = round(speedx / abs(speedx)) * rnd(2, 6)
    if canv.coords(ball1)[3] >= canv_height  or canv.coords(ball1)[3] <= 0 + 2 * r1:
        speedy1 = -speedy1
        speedx1 = round(speedx1 / abs(speedx1)) * rnd(2, 6)
    if canv.coords(ball2)[3] >= canv_height  or canv.coords(ball2)[3] <= 0 + 2 * r2:
        speedy2 = -speedy2
        speedx2 = round(speedx2 / abs(speedx2)) * rnd(2, 6)     
    if canv.coords(ball3)[3] >= canv_height  or canv.coords(ball3)[3] <= 0:
        speedy3 = -speedy3
        speedx3 = choice([-9, -6, -7, -8, 8, 7, 6, 9, 0])    
    


    
def click(event):

    global ball_cought

    print(event.x, event.y)
    print(x, y, r)

    if event.x in range(x - r, x + r) and event.y in range(y - r, y + r):
        ball_cought +=1
        canv.delete(ball)
        new_ball()    
    if event.x in range(x1 - r1, x1 + r1) and event.y in range(y1 - r1, y1 + r1):
        ball_cought +=1
        canv.delete(ball1)
        new_ball1()    
    if event.x in range(x2 - r2, x2 + r2) and event.y in range(y2 - r2, y2 + r2):
        ball_cought +=1
        canv.delete(ball2)
        new_ball2()    
    if event.x in range(x3 - r3, x3 + r3) and event.y in range(y3 - r3, y3 + r3):
        ball_cought +=5
        canv.delete(ball3)
        new_ball3()

    count.delete(ALL)
    count.create_text(count_width // 2, count_height // 2, text=str(ball_cought),
                justify=CENTER, font="Verdana 20")

new_ball()
new_ball1()
new_ball2()
new_ball3()
ball_motion()

canv.bind('<Button-1>', click)
mainloop()