""" Нарисуйте, используя модуль turtle число:
1973
"""

from turtle import *

t = Turtle()

t.screen.setup(800, 800)

for one in range(1):
    t.down()
    t.width(10)
    t.right(130)
    t.fd(30)
    t.bk(30)
    t.left(40)
    t.fd(100)
    t.up()

for nine in range(1):
    t.goto(20, -100)
    t.down()
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.up()

for seven in range(1):
    t.goto(90, 0)
    t.down()
    t.fd(50)
    t.right(110)
    t.fd(105)
    t.right(70)
    t.up()

for three in range(1):
    t.goto(160, 0)
    t.down()
    t.bk(50)
    t.left(60)
    t.fd(60)
    t.right(60)
    t.bk(30)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(50)

t.screen.exitonclick()
t.screen.mainloop()