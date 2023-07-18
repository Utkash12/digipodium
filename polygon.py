from turtle import *
def square():
    for i in range(4):
        forward(100)
        right(90)

def pentagon():
    for i in range(5):
        forward(100)
        right(72)

#calling
square()
pentagon()
goto(200,0)
square()
pentagon()

hideturtle()
mainloop()