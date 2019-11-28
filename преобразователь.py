
from tkinter import *

root = Tk()
c = Canvas(root, width =100, height = 200)
c.pack()
e = Entry(width=20)
b = Button(text="Преобразовать")
l = Label(bg='black', fg='white', width=20)

def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)

e.pack()
b.pack()
l.pack()
root.mainloop()