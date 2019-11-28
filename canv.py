from tkinter import*
root2 = Tk()
root2.geometry('600x600')

ending = Canvas(root2, width = 400, height = 500 * 2,bg='blue')
ending.pack(side = BOTTOM)
end = Canvas(root2, width = 300, height = 400 * 2,bg='blue')
end.pack()
ending.create_text(400 // 2, 500 // 2, text='Введи свое имя, победитель, ты заработал ' + str(1),
            justify=CENTER, font="Verdana 20")

e = Entry(ending, width=50)
b = Button(ending, text="Подтвердить")
def rewrite():
    pass

b.bind('<Button-1>', rewrite)
b.pack(side = BOTTOM)
e.pack(side = BOTTOM)
root2.mainloop()