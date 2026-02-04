from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(2):
    fd(5*m)
    lt(90)
    bk(13*m)
    lt(90)
up()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
down()
for _ in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-10, 6):
    for y in range(-16, 1):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(5*13 + 11 * 7 - 5 * 2)
done()