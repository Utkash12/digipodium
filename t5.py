from turtle import *
pencolor('yellow')
pensize(2)
bgcolor('black')

for i in range(16):
    pencolor('orange')
    fd(100)
    rt(360/16)
    for i in range(16):
        pencolor('pink')
        fd(50)
        rt(360/16)

hideturtle()
mainloop() # hold the window open