from turtle import *

tracer(False)

m = 20 # масштаб

screensize(5000, 5000)

for _ in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(7*m)
lt(90)
down()
for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()

for x in range(5, 11):
    for y in range(-14, -6):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(18*10 + 10*7 - 6 * 8)
done()