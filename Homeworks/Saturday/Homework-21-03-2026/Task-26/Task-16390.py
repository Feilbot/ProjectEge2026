with open(r'..\..\..\..\Files\26_16390.txt') as file:
    info = file.readline()
    boxes = sorted(int(i) for i in file)

V = int(info.split()[0])

cnt = 0
last_box = 0

for box in boxes:
    if V - box >= 0:
        V -= box
        cnt += 1
        last_box = box

while last_box + V not in boxes and V > 0:
    V -= 1

print(cnt, last_box + V)