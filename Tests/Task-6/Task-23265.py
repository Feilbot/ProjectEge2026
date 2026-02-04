from turtle import *

tracer(False)

m = 20

screensize(5000, 5000)

lt(90)
for _ in range(2):
    fd(20*m)
    lt(270)
    fd(12*m)
    rt(90)
up()
fd(9*m)
rt(90)
fd(7*m)
lt(90)
down()
for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()

for x in range(7, 13):
    for y in range(9, 21):
        goto(x*m, y*m)
        dot(5, 'red')
update()
print(21*13+14*7-12*6)
done()