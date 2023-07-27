import pgzrun

# screen size
WIDTH = 1000
HEIGHT= 500

# objects
p=Actor('hero')
e=Actor('enemy')
c=Actor('fruit')

def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()

def update(dt):
    print(dt)

# game loop
pgzrun.go()