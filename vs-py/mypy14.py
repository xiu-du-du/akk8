# 当前时间:2021/9/18 0:22
import turtle
t=turtle.Pen()
colors=("red","black","blue","green")
t.width(3)
t.speed(10)
for i in range(10):
    t.penup()
    t.goto(-500,500-i*50)
    t.pendown()
    t.goto(-50,500-i*50)

for i in range(10):
    t.penup()
    t.goto(-500+i*50, 500)
    t.pendown()
    t.goto(-500+i*50, 50)
turtle.done()


