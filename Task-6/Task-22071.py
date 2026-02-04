from turtle import *

tracer(False)

m = 200 # масштаб

screensize(50000, 50000)

lt(90)
fd(30*m)
lt(60)
fd(24*m)
rt(240)
fd(54*m)
lt(120)
fd(24*m)
lt(60)
up()
fd(30*m)
rt(90)
fd(20*m)
lt(90)
down()
for _ in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)

up()
for x in range(-21, 21):
    for y in range(30, 37):
        goto(x*m, y*m)
        dot(8, 'white')
update()
print(((10.6+21)/2*6).__floor__())
done()