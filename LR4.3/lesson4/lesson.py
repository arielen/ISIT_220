""" Нарисуйте следующую фигуру, используя модуль turtle. """
import turtle as t

t.setup(800, 800)
t.width(1)
t.speed(20)
t.bgcolor('#00ff00')

for green_quad in range(12):  # 12-углов
    t.begin_fill()
    t.goto(0, 0)
    t.right(90)
    t.fd(50)
    t.right(45)
    t.fd(30)
    t.right(90)
    t.fd(30)

    t.color('black', 'blue')  # green - стал голубым)
    t.end_fill()

t.home()

for yellow_quad in range(6):
    t.begin_fill()
    t.goto(0, 0)
    t.right(105)
    t.fd(50)
    t.right(90)
    t.fd(20)
    t.right(45)
    t.fd(20)
    t.goto(0, 0)
    t.left(179)
    t.color('black', 'yellow')
    t.end_fill()
t.home()
for red_quad in range(6):
    t.begin_fill()
    t.goto(0, 0)
    t.right(90)
    t.fd(50)
    t.right(45)
    t.fd(15)
    t.right(90)
    t.fd(15)
    t.goto(0, 0)
    t.left(165)
    t.color('black', 'red')
    t.end_fill()

t.exitonclick()
t.mainloop()
