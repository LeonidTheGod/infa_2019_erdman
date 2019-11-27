from graph import * 

width = 500
height = 600

windowSize(width, height)

def rect(x,y,x1,y1, color):
    brushColor(color)
    rectangle(x,y,x1,y1)

def window(x,y):
    penColor('#57cdde')
    color = ('#57cdde')
    rect(x, y, x + 55, y + 45, color)
    rect(x + 65, y, x + 55 + 65, y + 45, color)
    rect(x, y + 55, x + 55, y + 155, color)
    rect(x + 65, y + 55, x + 55 + 65, y + 155, color)

cat_move = []
def cat(x,y,r,bc):
    penColor('black')
    brushColor(bc)
    global cat_move 
     
    def tail():
        cat1 = el(x+r*2.5,y,r- 0.6*r,4)
        cat_move.append(cat1)
    def body():
        cat2 = el(x, y, r,2.2,1.1)
        cat_move.append(cat2)
        ################################ leg back
        cat3 = circle(x+r*1.6,y+ r//2, r//1.6)
        cat_move.append(cat3)
        cat4 = el(x+r*2.1,y+ r*1.4, r//4, 1, 2.5)
        cat_move.append(cat4)
        ################################ legs fd
        cat5 = el(x - r * 1.6, y + r // 1.2, r // 3.7, 1.7)
        cat_move.append(cat5)
        cat6 = el(x - r * 2.3, y + r // 2.9 , r // 3.7, 1, 1.7)
        cat_move.append(cat6)
    def head():
        # circle
        cat7 = circle(x-r*2, y-r//4, r//1.2)
        cat_move.append(cat7)
        # eyes 
        if bc == '#c87137':
            brushColor('#88aa00')
        cat8 = el(x - r * 2.35, y - r // 7, r // 5, 1, 1.2)
        cat_move.append(cat8)
        cat9 = el(x - r * 1.75, y - r // 7, r // 5, 1, 1.2)
        cat_move.append(cat9)
        brushColor('black')
        cat10 = el(x - r * 2.31, y - r // 7, r // 30, 1, 6)
        cat_move.append(cat10)
        cat11 = el(x - r * 1.71, y - r // 7, r // 30, 1, 6)
        cat_move.append(cat11) 
        # zrachki 
        brushColor('white')
        penColor('white')
        cat12 = el(x - r * 2.40, y - r // 4.5, r // 30, 1 )
        cat_move.append(cat12)
        cat13 = el(x - r * 1.80, y - r // 4.5, r // 30, 1)
        cat_move.append(cat13)
        # ears
        brushColor(bc)
        penColor('black')
        cat14 = polygon([(x - r * 1.5, y - r // 0.8), (x - r * 1.9, y - r // 0.99),
        (x - r * 1.6, y - r // 1.3), (x - r * 1.5, y - r // 0.8) ])
        cat_move.append(cat14)
        cat15 = polygon([(x - r * 2.7, y - r // 1.5), (x - r * 2.8, y - r // 0.9),
        (x - r * 2.3, y - r // 1.1), (x - r * 2.7, y - r // 1.5) ])
        cat_move.append(cat15)

    tail()
    body()
    head()

rect(0,0,width, height * 0.45, '#554400')
rect(0,height * 0.45,width,height, '#806600')

rast = -80
for i in range(3):
    rect(rast, 20, rast + width // 3.5, height // 3 , '#d5ffe6')
    rast += width // 3.5 + 60
for i in -69, 133, 335:
    window(i, 30)

x = 300
y = 300
r = 30
cat(300,300,30,'#c87137')
cat(200,400,20,'#c87137')
def update(): 

    for i in cat_move:
        moveObjectBy(i, -1, 0)
       
onTimer(update, 80)



run()