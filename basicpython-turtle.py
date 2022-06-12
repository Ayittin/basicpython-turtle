import turtle
colors =['red', 'purple','blue', 'green', 'orange', 'yellow'] #สีของปากกา
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
turtle.bgcolor('black') #ทำพื้นหลังเป็นสีดำ

for i in range(100):
    tao.pencolor(colors[i%6])
    tao.width (i//50 + 1)
    tao.forward(i)
    tao.left(59)

tao.penup()
tao.fd(100)
tao.right(90)
tao.goto(200,200)
tao.pendown()


def sqrfunce(size):
    for i in range(6):
        tao.fd(size)
        tao.pencolor(colors[i%6])
        tao.left(90)
        size = size-2

sqrfunce(146)
sqrfunce(126)
sqrfunce(106)
sqrfunce(86)
sqrfunce(66)
sqrfunce(46)
sqrfunce(26)

tao.penup()
tao.right(90)
tao.pendown()
sqrfunce(146)
sqrfunce(126)
sqrfunce(106)
sqrfunce(86)
sqrfunce(66)
sqrfunce(46)
sqrfunce(26)

tao.penup()
tao.right(90)
tao.pendown()
sqrfunce(146)
sqrfunce(126)
sqrfunce(106)
sqrfunce(86)
sqrfunce(66)
sqrfunce(46)
sqrfunce(26)

tao.penup()
tao.right(90)
tao.pendown()
sqrfunce(146)
sqrfunce(126)
sqrfunce(106)
sqrfunce(86)
sqrfunce(66)
sqrfunce(46)
sqrfunce(26)
