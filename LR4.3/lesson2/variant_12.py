""" Нарисуйте, используя модуль turtle число:
1825
"""
import turtle as t

t.setup(800, 800)
t.width(5)
t.color('#ff0004')
t.speed(2)

for one in range(1):
    t.goto(0, 0)
    t.down()
    t.right(120)
    t.fd(30)
    t.bk(30)
    t.left(30)
    t.fd(100)
    t.left(90)
    t.up()

for eight in range(1):
    t.goto(20, 0)
    t.down()
    t.right(90)
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
    t.right(180)
    t.up()

for two in range(1):
    t.goto(90, 0)
    t.down()
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

for five in range(1):
    t.goto(160, 0)
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

t.exitonclick()
t.mainloop()
