from turtle import *

tracer(False)

m = 40

screensize(5000, 5000)

lt(90)
rt(90)
for _ in range(3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)
for _ in range(2):
    rt(90)
    fd(10*m)
up()

for x in range(-14, 8):
    for y in range(-14, 8):
        goto(x*m, y*m)
        dot(3, 'red')
update()
print(203)
done()