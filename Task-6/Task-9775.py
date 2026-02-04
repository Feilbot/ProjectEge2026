from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(8*m)
rt(90)
bk(3*m)
lt(90)
down()
for _ in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()
for x in range(8, 14):
    for y in range(-5, 1):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(13*20 + 16*8 - 6*6)
done()