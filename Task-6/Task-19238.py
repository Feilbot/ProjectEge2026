from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for _ in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()
for x in range(5, 17):
    for y in range(-22, -4):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(12 * 18)
done()