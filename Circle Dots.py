import turtle as t
t.speed(200)
def f1():
    t.backward(200)
    t.dot()
    for i in range(20):
        t.forward(20)
        t.dot()
    t.goto(0,0)
f1()
d1=0
while d1<180:
    t.right(2)
    f1()
    d1+=2
t.right(90)
z=0
for i in range(1,11):
    t.goto(20+z,0)
    t.circle(20*i)
    z+=20
t.mainloop()
