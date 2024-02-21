import turtle
t=turtle.Turtle()
t.dot()
t.backward(200)
for i in range(20):
    t.dot()
    t.forward(20)
    t.dot()
t.goto(0,0)
t.lt(90)
t.backward(200)
for i in range(20):
    t.dot()
    t.forward(20)
    t.dot()
t.goto(0,0)
t.pensize(2)
x=0
t.pencolor('red')
y=200
i=20#1st quadrant
while i<200:
    t.goto(x+i,0)
    t.goto(0,y)
    y-=20
    t.goto(0,y)
    i+=20
    t.goto(x+i,0)
t.goto(0,0)
x=0
t.pencolor('green')
y=200
i=20
while i<200:
    t.goto(x-i,0)
    t.goto(0,y)
    y-=20
    t.goto(0,y)
    i+=20
    t.goto(x-i,0)
t.goto(0,0)
x=0
t.pencolor('blue')
y=-200
i=20#3st quadrant
while i<200:
    t.goto(x-i,0)
    t.goto(0,y)
    y+=20
    t.goto(0,y)
    i+=20
    t.goto(x-i,0)
t.goto(0,0)
x=0
t.pencolor('pink')
y=-200
i=20#4st quadrant
while i<200:
    t.goto(x+i,0)
    t.goto(0,y)
    y+=20
    t.goto(0,y)
    i+=20
    t.goto(x+i,0)
t.goto(0,0)
