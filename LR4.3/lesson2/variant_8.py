""" Нарисуйте, используя модуль turtle число:
6832
"""
from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(5)
t.color('#ff0004')

for six in range(1):
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

for eight in range(1):
    t.goto(20, 0)
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
    t.up()

for three in range(1):
    t.goto(90, 0)
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

for two in range(1):
    t.goto(160, 0)
    t.down()
    t.bk(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.up()

t.screen.exitonclick()
t.screen.mainloop()
