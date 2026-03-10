from turtle import *

tracer(False)

m = 20 # масштаб
lt(90)

screensize(5000, 5000)

for _ in range(9):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
bk(10 * m)
rt(90)
down()
for _ in range(8):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
up()
fd(6 * m)
lt(90)
down()
for _ in range(7):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)

up()
for x in range(10, 20):
    for y in range(10, 16):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(9 * 5)
done()