""" Нарисуйте, используя модуль turtle число:
5438
"""

from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(5)

for five in range(1):
    t.down()
    t.right(180)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.up()

for fourth in range(1):
    t.goto(20, 0)
    t.down()
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.bk(100)
    t.up()

for three in range(1):
    t.goto(90, 0)
    t.down()
    t.right(90)
    t.fd(50)
    t.left(60)
    t.bk(50)
    t.right(60)
    t.fd(25)
    t.right(90)
    t.fd(55)
    t.right(90)
    t.fd(50)
    t.up()

for eight in range(1):
    t.goto(160, 0)
    t.down()
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.bk(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)



t.screen.exitonclick()
t.screen.mainloop()
