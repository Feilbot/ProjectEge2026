from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

lt(90)
for _ in range(2):
    fd(14*m)
    lt(270)
    bk(12*m)
    rt(90)
up()
fd(9*m)
rt(90)
bk(7*m)
lt(90)
down()
for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-7, 0):
    for y in range(9, 15):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(15*13+14*7-7*6)
done()