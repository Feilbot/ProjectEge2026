from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

rt(270)
for _ in range(2):
    fd(8*m)
    rt(120)
rt(120)
for _ in range(2):
    rt(120)
    fd(3*m)
    rt(240)
rt(240)
for _ in range(2):
    fd(14*m)
    rt(120)
up()
for x in range(0, 13):
    for y in range(-6, 9):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print('ОТВЕТ:', 0.5 * 13 * 15)
done()