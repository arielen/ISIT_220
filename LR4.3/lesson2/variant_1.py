""" Нарисуйте, используя модуль turtle число:
2516
"""
from turtle import *

t = Turtle()
t.screen.setup(800, 800)
for two in range(1):
    t.width(10)
    t.fd(50)
    t.left(90)
    t.bk(50)
    t.right(90)
    t.bk(50)
    t.left(90)
    t.bk(50)
    t.left(90)
    t.bk(50)
    t.up()

t.goto(120, 0 )
for five in range(1):
    t.down()
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

t.goto(160, 0)
for one in range(1):
    t.down()
    t.left(60)
    t.fd(30)
    t.bk(30)
    t.left(30)
    t.fd(100)
    t.up()

t.goto(240, 0)
for six in range(1):
    t.down()
    t.right(90)
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

t.screen.exitonclick()
t.screen.mainloop()
