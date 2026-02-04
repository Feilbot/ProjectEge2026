from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(2):
    fd(23*m)
    lt(90)
    bk(27*m)
    lt(90)
up()
bk(5*m)
rt(90)
fd(11*m)
lt(90)
down()
for _ in range(2):
    fd(26 * m)
    rt(90)
    fd(32 * m)
    rt(90)

up()
for x in range(0, 22):
    for y in range(-27, -10):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(23*27 + 26 * 32 - 22 * 17)
done()