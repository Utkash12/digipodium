from turtle import *
speed(1)

def polygon(sides, length, color, width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

polygon(4, 100, "red", 5)
goto(200,0)
polygon(6,50,"green",2)
goto(200,200)
polygon(3,100,"blue",10)

hideturtle()
mainloop()