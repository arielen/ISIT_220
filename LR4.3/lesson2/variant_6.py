""" Нарисуйте, используя модуль turtle число:
9735
"""
from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(5)
t.color('#ff0004')

for nine in range(1):
    t.down()
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
    t.goto(70, 100)
    t.down()
    t.fd(50)
    t.right(110)
    t.fd(105)
    t.right(70)
    t.up()

for three in range(1):
    t.goto(140, 100)
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
    t.up()

for five in range(1):
    t.goto(210, 0)
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

t.screen.exitonclick()
t.screen.mainloop()