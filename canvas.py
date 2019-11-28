from tkinter import *
root = Tk()

c = Canvas(root, width=800, height=500, bg='white')
c.pack()
# создаем отрезок
c.create_line(10, 10, 190, 50)
# создаем стрелку
c.create_line(100, 180, 100, 60, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 30 10")
c.create_rectangle(10, 10, 190, 60)

c.create_polygon(500, 10, 420, 90, 580, 90)

c.create_polygon(40, 110, 160, 110, 190, 180, 10, 180,
                fill='orange', outline='black')


c.create_oval(50, 350, 150,  450, width=2)
c.create_oval(100, 120, 190, 190, fill='blue', activefill='skyblue', activedash=(200,4), outline='black' )

c.create_arc(310, 310, 190, 190, start=0, extent=45, fill='red')
c.create_arc(310, 310, 190, 190, start=180, extent=25, fill='orange')
c.create_arc(310, 310, 190, 190, start=240, extent=100, style=CHORD, fill='green')
c.create_arc(310, 310, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)


c.create_text(100, 100, text="Hello World,\nPython\nand Tk",
                justify=CENTER, font="Verdana 14")
c.create_text(200, 200, text="About this",
                anchor=N, fill="grey")



root.mainloop()