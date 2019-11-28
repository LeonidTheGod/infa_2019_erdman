from tkinter import *
from random import randrange as rnd, choice
import time
from tkinter import Tk, Label, Button

timer_seconds = 30
ROOT = Tk()


def timer_tick():

    global timer_seconds
    if timer_seconds:
        timer.after(1000, timer_tick)
        timer_seconds -= 1


colors = ['red', 'orange', 'yellow', 'green', 'blue']
FRIGHT = LabelFrame(text='BEST SCORES')
FLEFT = LabelFrame(text='Game')
FRIGHT.pack(side=LEFT)
FLEFT.pack()
root_x, root_y = 1000, 600
BALL_COUGHT = 0
COUNT_WIDTH, COUNT_HEIGHT = 60, 50
CANV_WIDTH, CANV_HEIGHT = 700, 500
SCOR_WIDTH, SCOR_HEIGHT = 200, CANV_HEIGHT - 100
ROOT_GEOM = str(root_x) + 'x' + str(root_y)
ROOT.geometry(ROOT_GEOM)

CANV = Canvas(FLEFT, width=CANV_WIDTH, height=CANV_HEIGHT, bg='ivory')
COUNT = Canvas(FRIGHT, width=COUNT_WIDTH, height=COUNT_HEIGHT, bg='ivory')
SCORE = Canvas(FRIGHT, width=SCOR_WIDTH, height=SCOR_HEIGHT, bg='ivory')
TIMING = Canvas(FRIGHT, width=COUNT_WIDTH*2, height=COUNT_HEIGHT, bg='ivory')

speedx = rnd(2, 6)
speedy = rnd(2, 6)
speedx1 = rnd(2, 6)
speedy1 = rnd(2, 6)
speedx2 = rnd(2, 6)
speedy2 = rnd(2, 6)
speedx3 = choice([-9, -8, -7, -6, 0, 6, 7, 8, 9])
speedy3 = choice([-9, -8, -7, -6, 0, 6, 7, 8, 9])

SCORE.pack(side=TOP)
COUNT.pack(side=BOTTOM)
TIMING.pack(side=BOTTOM)
CANV.pack(side=RIGHT)
step_y = SCOR_HEIGHT // 10
step = 40

timer = Label(FRIGHT)
timer.pack(side=RIGHT)
timer_tick()

f = open(r'score.txt', encoding='utf-8').readlines()

scores = []
names = []

for line in f:
    SCORE.create_text(SCOR_WIDTH // 2, step, text=str(line),
                      justify=LEFT, font="Verdana 14")
    step += step_y
    line = line.split()
    names.append(line[0])
    scores.append(int(line[-1]))


def new_ball():
    global x, y, r, ball
    r = rnd(10, 50)
    x = rnd((root_x - CANV_WIDTH) / 2 - 4 * r,
            (root_x - CANV_WIDTH) / 2 + CANV_WIDTH - r * 9)
    y = rnd(50, 450)
    ball = CANV.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors))


def new_ball1():
    global x1, y1, r1, ball1
    r1 = rnd(10, 50)
    x1 = rnd((root_x - CANV_WIDTH) / 2 + 4 * r1,
             (root_x - CANV_WIDTH) / 2 + CANV_WIDTH - r1 * 9)
    y1 = rnd(50, 450)
    ball1 = CANV.create_oval(x1 - r1, y1 - r1, x1 + r1,
                             y1 + r1, fill=choice(colors))


def new_ball2():
    global x2, y2, r2, ball2
    r2 = rnd(10, 50)
    x2 = rnd((root_x - CANV_WIDTH) / 2 + 4 * r2,
             (root_x - CANV_WIDTH) / 2 + CANV_WIDTH - r2 * 9)
    y2 = rnd(50, 450)
    ball2 = CANV.create_oval(x2 - r2, y2 - r2, x2 + r2,
                             y2 + r2, fill=choice(colors))


def new_ball3():
    global x3, y3, r3, ball3
    r3 = rnd(10, 30)
    x3 = rnd((root_x - CANV_WIDTH) / 2 + 4 * r3,
             (root_x - CANV_WIDTH) / 2 + CANV_WIDTH - r3 * 9)
    y3 = rnd(50, 450)
    ball3 = CANV.create_rectangle(
        x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill=choice(colors))


def ball_motion():

    global speedx, speedy, x, y, r, koko
    global speedx1, speedy1, x1, y1, r1
    global speedx2, speedy2, x2, y2, r2
    global speedx3, speedy3, x3, y3, r3

    CANV.move(ball, speedx, speedy)
    CANV.move(ball1, speedx1, speedy1)
    CANV.move(ball2, speedx2, speedy2)
    CANV.move(ball3, speedx3, speedy3)

    ROOT.after(10, ball_motion)

    x += speedx
    y += speedy
    x1 += speedx1
    y1 += speedy1
    x2 += speedx2
    y2 += speedy2
    x3 += speedx3
    y3 += speedy3

    if CANV.coords(ball)[2] >= CANV_WIDTH or CANV.coords(ball)[2] <= 0 + 2 * r:
        speedx = -speedx
        speedy = round(speedy / abs(speedy)) * rnd(2, 6)
    if CANV.coords(ball1)[2] >= CANV_WIDTH or CANV.coords(ball1)[2] <= 0 + 2 * r1:
        speedx1 = -speedx1
        speedy1 = round(speedy1 / abs(speedy1)) * rnd(2, 6)
    if CANV.coords(ball2)[2] >= CANV_WIDTH or CANV.coords(ball2)[2] <= 0 + 2 * r2:
        speedx2 = -speedx2
        speedy2 = round(speedy2 / abs(speedy2)) * rnd(2, 6)
    if CANV.coords(ball3)[2] >= CANV_WIDTH or CANV.coords(ball3)[2] <= 0 + 2 * r3:
        speedx3 = -speedx3
        speedy3 = choice([-9, -8, -7, -6, 0, 6, 7, 8, 9])

    if CANV.coords(ball)[3] >= CANV_HEIGHT or CANV.coords(ball)[3] <= 0 + 2 * r:
        speedy = -speedy
        speedx = round(speedx / abs(speedx)) * rnd(2, 6)
    if CANV.coords(ball1)[3] >= CANV_HEIGHT or CANV.coords(ball1)[3] <= 0 + 2 * r1:
        speedy1 = -speedy1
        speedx1 = round(speedx1 / abs(speedx1)) * rnd(2, 6)
    if CANV.coords(ball2)[3] >= CANV_HEIGHT or CANV.coords(ball2)[3] <= 0 + 2 * r2:
        speedy2 = -speedy2
        speedx2 = round(speedx2 / abs(speedx2)) * rnd(2, 6)
    if CANV.coords(ball3)[3] >= CANV_HEIGHT or CANV.coords(ball3)[3] <= 0 + 2 * r3:
        speedy3 = -speedy3
        speedx3 = choice([-9, -8, -7, -6, 0, 6, 7, 8, 9])
    if timer_seconds <= 0:
        ROOT.destroy()

    TIMING.delete(ALL)
    TIMING.create_text(COUNT_WIDTH, COUNT_HEIGHT // 2, text='00:'+str(timer_seconds),
                       justify=CENTER, font="Verdana 20")


COUNT.create_text(COUNT_WIDTH // 2, COUNT_HEIGHT // 2, text=str(BALL_COUGHT),
                  justify=CENTER, font="Verdana 20")


def rep(event):
    global x, y, x1, y1,  x2, y2, x3, y3
    CANV.delete(ALL)
    new_ball()
    new_ball1()
    new_ball2()
    new_ball3()


def click(event):

    global BALL_COUGHT

    if event.x in range(x - r, x + r) and event.y in range(y - r, y + r):
        BALL_COUGHT += 1
        CANV.delete(ball)
        new_ball()
    if event.x in range(x1 - r1, x1 + r1) and event.y in range(y1 - r1, y1 + r1):
        BALL_COUGHT += 1
        CANV.delete(ball1)
        new_ball1()
    if event.x in range(x2 - r2, x2 + r2) and event.y in range(y2 - r2, y2 + r2):
        BALL_COUGHT += 1
        CANV.delete(ball2)
        new_ball2()
    if event.x in range(x3 - r3, x3 + r3) and event.y in range(y3 - r3, y3 + r3):
        BALL_COUGHT += 5
        CANV.delete(ball3)
        new_ball3()

    COUNT.delete(ALL)
    COUNT.create_text(COUNT_WIDTH // 2, COUNT_HEIGHT // 2, text=str(BALL_COUGHT),
                      justify=CENTER, font="Verdana 20")


new_ball()
new_ball1()
new_ball2()
new_ball3()
ball_motion()

CANV.bind('<Button-1>', click)
ROOT.bind('<r>', rep)

mainloop()

''' ---------------------------------------------------------------------------------------------------------------'''

if BALL_COUGHT >= min(scores):
    root2 = Tk()
    root2.geometry(ROOT_GEOM)
    ending = Canvas(root2, width=CANV_WIDTH, height=CANV_HEIGHT * 2)
    end = Canvas(root2, width=CANV_WIDTH, height=CANV_HEIGHT * 2)
    ending.pack(side=BOTTOM)
    end.pack(side=TOP)
    end.create_text(CANV_WIDTH // 2, CANV_HEIGHT // 2, text='Введи свое имя, победитель, ты заработал ' + str(BALL_COUGHT),
                    justify=CENTER, font="Verdana 20")
    e = Entry(ending, width=50)
    b = Button(ending, text="Подтвердить")

    def rewrite(event):

        s = e.get()
        scores.append(BALL_COUGHT)

        if BALL_COUGHT != min(scores):
            f = open('score.txt', 'w', encoding='utf-8')
            scores.sort(reverse=True)

            ind = scores.index(BALL_COUGHT)
            names.insert(ind, s)
            names.pop(10)
            scores.pop(10)

            for i in range(10):
                f.write(names[i] + ' ' + str(scores[i])+'\n')
            exit()
    b.bind('<Button-1>', rewrite)
    b.pack(side=BOTTOM)
    e.pack(side=BOTTOM)
    root2.mainloop()
