from tkinter import *
from random import randrange as rnd, choice
import time
from tkinter import Tk, Label, Button

timer_seconds = 30

def timer_tick():

    global timer_seconds
    if timer_seconds:
        timer.after(1000, timer_tick)
        timer_seconds -= 1


root = Tk()

f_top = LabelFrame(text= 'BEST SCORES')
f_bot = LabelFrame(text= 'Game')
f_top.pack(side = LEFT)
f_bot.pack()
colors = ['red','orange','yellow','green','blue']
root_x, root_y = 1000, 600
ball_cought = 0
count_width, count_height = 60, 50
canv_width, canv_height = 700, 500
score_width, score_height = 200, canv_height - 100
root_geom = str(root_x) + 'x' + str(root_y)
root.geometry(root_geom)
canv = Canvas(f_bot, width= canv_width, height = canv_height,bg='ivory')
count = Canvas(f_top, width= count_width, height = count_height ,bg='ivory')
score = Canvas(f_top, width= score_width, height = score_height ,bg='ivory')
timing = Canvas(f_top, width= count_width*2, height = count_height ,bg='ivory')

score.pack(side = TOP)
count.pack(side = BOTTOM)
timing.pack(side = BOTTOM)
canv.pack(side = RIGHT)
step_y = score_height // 10
step = 40

timer = Label(f_top)
timer.pack(side = RIGHT)
timer_tick()

f = open(r'score.txt', encoding='utf-8').readlines()

scores = []
names = []

for line in f:
    score.create_text(score_width // 2, step, text=str(line),
                justify=LEFT, font="Verdana 14")
    step += step_y
    line = line.split()
    names.append(line[0])
    scores.append(int(line[-1]))

speedx =rnd(2, 6)
speedy =rnd(2, 6)
speedx1 =rnd(2, 6)
speedy1 =rnd(2, 6)
speedx2 = rnd(2, 6)
speedy2 =rnd(2, 6)
speedx3 = choice([-9,-8,-7,-6,0,6,7,8,9])
speedy3= choice([-9,-8,-7,-6,0,6,7,8,9])

def new_ball():
    global x, y, r, ball
    r = rnd(10,50)
    x = rnd((root_x - canv_width) / 2 - 4 * r, (root_x - canv_width) / 2 + canv_width - r * 9 )
    y = rnd(50,450)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors))   
def new_ball1():
    global x1, y1, r1, ball1
    r1 = rnd(10,50)
    x1 = rnd((root_x - canv_width) / 2 + 4 * r1, (root_x - canv_width) / 2 + canv_width - r1 * 9 )
    y1 = rnd(50,450)
    ball1 = canv.create_oval(x1 -r1 ,y1 -r1 ,x1 +r1 ,y1 +r1 ,fill = choice(colors))   
def new_ball2():
    global x2, y2, r2, ball2
    r2 = rnd(10,50)
    x2 = rnd((root_x - canv_width) / 2 + 4 * r2, (root_x - canv_width) / 2 + canv_width - r2 * 9 )
    y2 = rnd(50,450)
    ball2 = canv.create_oval(x2 -r2 ,y2 -r2 ,x2 +r2 ,y2 +r2 ,fill = choice(colors)) 
def new_ball3():
    global x3, y3, r3, ball3
    r3 = rnd(10,30)
    x3 = rnd((root_x - canv_width) / 2 + 4 * r3, (root_x - canv_width) / 2 + canv_width - r3 * 9 )
    y3 = rnd(50,450)
    ball3 = canv.create_rectangle(x3 -r3 ,y3 -r3 ,x3 +r3 ,y3 +r3 ,fill = choice(colors))

def ball_motion():

    global speedx, speedy, x, y, r, koko
    global speedx1, speedy1, x1, y1, r1
    global speedx2, speedy2, x2, y2, r2
    global speedx3, speedy3, x3, y3, r3

    canv.move(ball, speedx, speedy)
    canv.move(ball1, speedx1, speedy1)
    canv.move(ball2, speedx2, speedy2)
    canv.move(ball3, speedx3, speedy3)

    root.after(10,ball_motion)

    x += speedx
    y += speedy    
    x1 += speedx1
    y1 += speedy1    
    x2 += speedx2
    y2 += speedy2    
    x3 += speedx3
    y3 += speedy3

    if canv.coords(ball)[2] >= canv_width or canv.coords(ball)[2] <= 0 + 2 * r:
        speedx = -speedx
        speedy = round(speedy / abs(speedy)) * rnd(2, 6)
    if canv.coords(ball1)[2] >= canv_width  or canv.coords(ball1)[2] <= 0 + 2 * r1:
        speedx1 = -speedx1
        speedy1 = round(speedy1 / abs(speedy1)) * rnd(2, 6)
    if canv.coords(ball2)[2] >= canv_width  or canv.coords(ball2)[2] <= 0 + 2 * r2:
        speedx2 = -speedx2
        speedy2 = round(speedy2 / abs(speedy2)) * rnd(2, 6)    
    if canv.coords(ball3)[2] >= canv_width  or canv.coords(ball3)[2] <= 0 + 2 * r3 :
        speedx3 = -speedx3
        speedy3 = choice([-9,-8,-7,-6,0,6,7,8,9])

    if canv.coords(ball)[3] >= canv_height or canv.coords(ball)[3] <= 0 + 2 * r:
        speedy = -speedy
        speedx = round(speedx / abs(speedx)) * rnd(2, 6)
    if canv.coords(ball1)[3] >= canv_height  or canv.coords(ball1)[3] <= 0 + 2 * r1:
        speedy1 = -speedy1
        speedx1 = round(speedx1 / abs(speedx1)) * rnd(2, 6)
    if canv.coords(ball2)[3] >= canv_height  or canv.coords(ball2)[3] <= 0 + 2 * r2:
        speedy2 = -speedy2
        speedx2 = round(speedx2 / abs(speedx2)) * rnd(2, 6)     
    if canv.coords(ball3)[3] >= canv_height  or canv.coords(ball3)[3] <= 0 + 2 * r3:
        speedy3 = -speedy3
        speedx3 = choice([-9,-8,-7,-6,0,6,7,8,9])  
    if timer_seconds <= 0:
        root.destroy()

    timing.delete(ALL)
    timing.create_text(count_width, count_height // 2, text='00:'+str(timer_seconds),
            justify=CENTER, font="Verdana 20")

count.create_text(count_width // 2, count_height // 2, text=str(ball_cought),
            justify=CENTER, font="Verdana 20")

def rep(event):
    global x, y, x1, y1,  x2, y2, x3, y3
    canv.delete(ALL)
    new_ball()
    new_ball1()
    new_ball2()
    new_ball3()



    
def click(event):

    global ball_cought

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
root.bind('<r>', rep)

mainloop()

''' ---------------------------------------------------------------------------------------------------------------'''

if ball_cought >= min(scores):
    root2 = Tk()
    root2.geometry(root_geom)
    ending = Canvas(root2, width = canv_width, height = canv_height * 2)
    end = Canvas(root2, width = canv_width, height = canv_height * 2)
    ending.pack(side = BOTTOM)
    end.pack(side = TOP)
    end.create_text(canv_width // 2, canv_height // 2, text='Введи свое имя, победитель, ты заработал ' + str(ball_cought),
                justify=CENTER, font="Verdana 20")
    e = Entry(ending, width=50)
    b = Button(ending, text="Подтвердить")

    def rewrite(event):
        
        s = e.get()
        scores.append(ball_cought)

        if ball_cought != min(scores):
            f = open('score.txt','w', encoding='utf-8')
            scores.sort(reverse=True)

            ind = scores.index(ball_cought)
            names.insert(ind, s)
            names.pop(10)
            scores.pop(10)

            for i in range(10):
                f.write(names[i] + ' ' + str(scores[i])+'\n')
            exit()
    b.bind('<Button-1>', rewrite)
    b.pack(side = BOTTOM)
    e.pack(side = BOTTOM)
    root2.mainloop()
