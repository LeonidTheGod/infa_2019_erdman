from random import randrange as rnd, choice
import tkinter as tk
import math
import time


f = open(r'C:\\Users\\kings\\Documents\\GitHub\\infa_2019_erdman\\cannon\\record.txt', encoding='utf-8').readlines()
record = int(f[0])



root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1000x600')
frame_game = tk.LabelFrame(root, width = 800, height = 600, text = 'game')
frame_left = tk.LabelFrame(root, width = 200, height = 600 , text = 'scores')
frame_scores = tk.LabelFrame(frame_left, width = 180, height = 400)
frame_scores.pack(side = 'top')
frame_game.pack(side = 'right')
frame_left.pack(side = 'left')
canv = tk.Canvas(frame_game, width = 800, height = 600, bg = 'ivory')
canv_scores = tk.Canvas(frame_scores, height = 400, bg = 'ivory')
canv_left = tk.Canvas(frame_left, width = 200, height = 600, bg = 'ivory')
rest = tk.Button(frame_left, text = 'Restart', width = 180, height = 180, bg = 'ivory', font= 'Verdana 20')
rest.pack()
canv_scores.pack()
canv.pack(expand = 1)
canv_left.pack( expand = 1)

canv_scores.create_text(100, 100, text='BEST SCORE:', font='48')



class ball():
    def __init__(self, x=40, y=450):

        self.count = 3
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.gravity = 1 * 1
        self.gravityx = self.gravity / 2 * 1
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id_ball = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id_ball,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move_ball(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y -= self.vy
        # self.set_coords()
        canv.move(self.id_ball, self.vx, -self.vy)

        if self.x >= 780:
            self.x -= self.vx

            self.vx = -self.vx // 2
        if self.x <= -120:
            canv.delete(self.id_ball)

            # balls.pop(0)
        if self.count > 0:
            if self.y >= 500:
                self.y -= 7
                self.count -= 1
                self.vy = -self.vy // 1.7

        elif self.count <= 0 and self.count >= -10:
            self.vy = 0
            self.vx = 0
            self.count -= 2
        else:
            canv.delete(self.id_ball)

            # balls.pop(0)

        if self.count > 0:
            self.vy -= self.gravity
        if self.vx > 1:
            if self.count != 3:
                self.vx -= self.gravityx / 2
            else:
                self.vx -= self.gravityx / 4

    def hittest(self, target):

        if round(self.x) in range(target.x - target.r - self.r, target.x + target.r + self.r) \
                and round(self.y) in range(target.y - target.r - self.r, target.y + target.r + self.r):
            return True


class gun():

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1
    def fire2_start_super(self, event):
        self.f2_on = 2


    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        if event.x - new_ball.x != 0:
            self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        else:
            self.an = 1

        new_ball.vx = self.f2_power * math.cos(self.an) * 1
        new_ball.vy = - self.f2_power * math.sin(self.an) * 1
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x-20) != 0:
                self.an = math.atan((event.y-450) / (event.x-20))
            else:
                self.an = 1
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on == 1:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        elif self.f2_on == 2:
            if self.f2_power < 50:
                self.f2_power += 10
            canv.itemconfig(self.id, fill='red')

        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self, points='yes'):
        self.color = 'red'
        self.points = 0
        self.live = 1
        self.vy = 10
        self.id = canv.create_oval(0, 0, 0, 0)
        if points == 'yes':
            self.id_points = canv.create_text(
                30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(500, 750)
        y = self.y = rnd(100, 450)
        r = self.r = rnd(2, 30)
        color = self.color
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move_target(self):

        canv.move(self.id, 0, self.vy)
        self.y += self.vy
        if self.y + self.r + self.vy >= 490:
            self.vy = -self.vy
        elif self.y - self.r <= 10:
            self.vy = -self.vy

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        t1.points += points
        canv.itemconfig(t1.id_points, text=t1.points)


t1 = target()
t2 = target('no')
t3 = target('no')
screen1 = canv.create_text(400, 300, text='', font='28')
record_count = canv_scores.create_text(100, 300, text=str(record), font='Verdana 40')
g1 = gun()
bullet = 0


def del_balls():

    global balls
    balls = []

def restart():
    t1.hit()
    t2.hit()
    t3.hit()

    for b in balls:
        canv.delete(b.id_ball)
    del_balls()
    t1.points = 0
    canv.itemconfig(t1.id_points, text=t1.points)
    root.after(1000, new_game)



def new_game(event=''):
    global gun, t1, screen1, balls, bullet, record, record_count
    targets = []
    balls = []
    canv.delete(screen1)
    canv_scores.delete(record_count)
    screen1 = canv.create_text(400, 300, text='', font='28')
    record_count = canv_scores.create_text(100, 300, text=str(record), font='Verdana 40')


    t1.new_target()
    t2.new_target()
    t3.new_target()

    targets = [t1, t2, t3]

    bullet = 0
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<Button-3>', g1.fire2_start_super)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    rest.config(command = restart)

    zzz = 0.03
    t1.live = 1
    t2.live = 1
    t3.live = 1
    while t1.live != 0 or t2.live != 0 or t3.live != 0 or balls:
        for target in targets:
            target.move_target()
            if target.live == 0:
                targets.remove(target)

        for b in balls:
            b.move_ball()

            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            elif b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            elif b.hittest(t3) and t3.live:
                t3.live = 0
                t3.hit()

            elif t1.live == 0 and t2.live == 0 and t3.live == 0:
                canv.bind('<Button-1>', g1.fire2_start)
                canv.bind('<ButtonRelease-1>', '')

                canv.itemconfig(
                    screen1, text='Вы уничтожили цели {}-м выстрелом'.format(bullet))
                root.after(2000, del_balls)

        time.sleep(zzz)
        canv.update()
        g1.targetting()
        g1.power_up()
    canv.delete(b.id_ball)
    canv.delete(gun)
    if t1.points > record:
        record = t1.points
        open('C:\\Users\\kings\\Documents\\GitHub\\infa_2019_erdman\\cannon\\record.txt', 'w').write(str(record))

    root.after(2000, new_game)

new_game()

tk.mainloop()


