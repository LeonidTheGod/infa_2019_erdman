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

    
def cat(x,y,r,bc):
    penColor('black')
    brushColor(bc)
     
    def tail():
        el(x+r*2.5,y,r- 0.6*r,4)
    def body():

        el(x, y, r,2.2,1.1)
        ################################ leg back
        circle(x+r*1.6,y+ r//2, r//1.6)

        el(x+r*2.1,y+ r*1.4, r//4, 1, 2.5)
        ################################ legs fd
        el(x - r * 1.6, y + r // 1.2, r // 3.7, 1.7)
        el(x - r * 2.3, y + r // 2.9 , r // 3.7, 1, 1.7)
    def head():
        # circle
        circle(x-r*2, y-r//4, r//1.2)
        # eyes 
        if bc == '#c87137':
            brushColor('#88aa00')
        el(x - r * 2.35, y - r // 7, r // 5, 1, 1.2)
        el(x - r * 1.75, y - r // 7, r // 5, 1, 1.2)
        brushColor('black')
        el(x - r * 2.31, y - r // 7, r // 30, 1, 6)
        el(x - r * 1.71, y - r // 7, r // 30, 1, 6) 
        # zrachki 
        brushColor('white')
        penColor('white')
        el(x - r * 2.40, y - r // 4.5, r // 30, 1 )
        el(x - r * 1.80, y - r // 4.5, r // 30, 1)
        # ears
        brushColor(bc)
        penColor('black')
        polygon([(x - r * 1.5, y - r // 0.8), (x - r * 1.9, y - r // 0.99),
        (x - r * 1.6, y - r // 1.3), (x - r * 1.5, y - r // 0.8) ])
        polygon([(x - r * 2.7, y - r // 1.5), (x - r * 2.8, y - r // 0.9),
        (x - r * 2.3, y - r // 1.1), (x - r * 2.7, y - r // 1.5) ])




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

cat(300,300,30,'#c87137')
cat(400,400,20,'#c87137')
cat(200,500,20,'#c87137')

run()