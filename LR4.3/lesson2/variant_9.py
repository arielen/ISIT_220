""" Нарисуйте, используя модуль turtle число:
3549
"""
import turtle as t

t.setup(800, 800)
t.width(5)
t.color('#ff0004')
t.speed(2)

for three in range(1):
    t.down()
    t.fd(50)
    t.left(60)
    t.bk(60)
    t.right(60)
    t.fd(30)
    t.left(90)
    t.bk(50)
    t.right(90)
    t.bk(50)
    t.up()

for five in range(1):
    t.goto(70, 0)
    t.down()
    t.fd(50)
    t.bk(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(180)  # возвращаем исходное направление
    t.up()

for fourth in range(1):
    t.goto(140, 0)
    t.down()
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.bk(100)
    t.right(90)  # возвращаем на исходную
    t.up()

for nine in range(1):
    t.goto(210, -100)
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

t.exitonclick()
t.mainloop()
