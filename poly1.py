from turtle import *
def square():
    for i in range(4):
        forward(100)
        right(90)

def pentagon():
    for i in range(5):
        forward(100)
        right(72)

for i in range(5):
    square()
    pentagon()
    right(72)

hideturtle()
mainloop()