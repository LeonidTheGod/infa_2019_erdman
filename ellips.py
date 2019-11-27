from graph import *
def update(): 
  moveObjectBy(obj, 5, 0)
  if xCoord(obj) >= 380: # если вышел 
     close()             # за границу
onTimer(update, 50)
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()  # закрыть окно 
onKey(keyPressed)
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)
onKey(keyPressed)
onTimer(update, 50)
run()