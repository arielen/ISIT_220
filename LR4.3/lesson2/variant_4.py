""" Нарисуйте, используя модуль turtle число:
7264
"""
from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(5)

for seven in range(1):
    t.down()
    t.fd(50)
    t.right(110)
    t.fd(105)
    t.up()

for two in range(1):
    t.goto(70, 0)
    t.down()
    t.left(110)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.up()

for six in range(1):
    t.goto(190, 0)
    t.down()
    t.right(180)
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

for fourth in range(1):
    t.goto(210, 0)
    t.down()
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.bk(100)
    t.up()



t.screen.exitonclick()
t.screen.mainloop()
