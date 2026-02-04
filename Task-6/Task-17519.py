from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for _ in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(0, 22):
    for y in range(-1, 1):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(2 * 22)
done()