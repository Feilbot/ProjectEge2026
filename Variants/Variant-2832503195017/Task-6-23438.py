from turtle import *

tracer(False)
m = 10
screensize(2000, 2000)

lt(90)

for _ in range(5):
    fd(40 * m)
    rt(90)
    fd(46 * m)
    rt(90)
up()
fd(19 * m)
rt(90)
fd(19 * m)
lt(90)
down()
for _ in range(5):
    fd(37 * m)
    rt(90)
    fd(19 * m)
    rt(90)

up()
for x in range(0, 47):
    for y in range(0, 41):
        goto(x*m, y*m)
        dot(5, 'red')

for x in range(8, 28):
    for y in range(-16, 0):
        goto(x*m, y*m)
        dot(5, 'green')

print(20 * 16 + 47 * 41)

done()