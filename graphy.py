from graph import* 
brushColor('yellow')
circle(250, 250, 150)
brushColor('red')
circle(175, 200, 30)
circle(315, 200, 20)
brushColor('black')
circle(175, 200, 30 / 2)
circle(315, 200, 20 / 2)
polygon([(220, 170), (100, 120), (105, 95), (225,165)])
polygon([(500 - 220, 500 - 170), (500 - 100, 500 - 120), (500 - 105, 500 - 95), (500 - 225,500 - 165)])
rectangle(200 - 20, 300 + 20, 300 + 20, 350)

run()
