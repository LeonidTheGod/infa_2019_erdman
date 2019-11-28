from tkinter import Tk, Label, Button

timer_seconds = 310  # текущее положение таймера, сек

def timer_tick():
    global timer_seconds
    if timer_seconds:
        label.after(1000, timer_tick)
        timer_seconds -= 1
        show_timer()

def show_timer():
    '''отобразить таймер'''
    m = timer_seconds//60
    s = timer_seconds-m*60
    label['text'] = '%02d:%02d' % (m, s)
    print(timer_seconds)

root = Tk()
while timer_seconds or Button(root, text="Quit", command=root.destroy).pack():
    label = Label(root)
    label.pack()
    show_timer()
    timer_tick()
    print(timer_seconds)
    root.mainloop()
    