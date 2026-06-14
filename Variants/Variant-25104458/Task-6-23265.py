from turtle import *

screensize(2000, 2000)
tracer(False)

m = 20

lt(90)

for _ in range(2):
    fd(20 * m)
    lt(270)
    fd(12 * m)
    rt(90)

up()
fd(9 * m)
rt(90)
fd(7 * m)
lt(90)
down()

for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()

for x in range(0, 14):
    for y in range(0, 23):
        goto(x*m, y*m)
        dot(4, 'red')

print(13 * 21 + 26)

done()