from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

x = 20
for _ in range(4):
    fd(x*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24)
rt(90)
down()
for _ in range(4):
    fd(29*m)
    rt(90)
    bk(18)
    rt(90)
up()
for x in range(0, 33):
    for y in range(-6, 9):
        goto(x*m, y*m)
        dot(8, 'white')
update()
print('ОТВЕТ: 20')
done()