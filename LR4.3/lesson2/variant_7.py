""" Нарисуйте, используя модуль turtle число:
4631
"""
from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(5)
t.color('#ff0004')
t.speed(2)

for fourth in range(1):
    t.down()
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.bk(100)
    t.up()

for six in range(1):
    t.goto(120, 0)
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

for three in range(1):
    t.goto(140, 0)
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

for one in range(1):
    t.goto(230, 0)
    t.down()
    t.left(60)
    t.fd(30)
    t.bk(30)
    t.left(30)
    t.fd(100)

t.screen.exitonclick()
t.screen.mainloop()
