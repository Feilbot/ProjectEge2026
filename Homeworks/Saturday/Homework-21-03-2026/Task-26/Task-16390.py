with open(r'..\..\..\..\Files\26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = sorted(int(i) for i in file)

cnt = 0
last_box = 0

for box in boxes:
    if S - box >= 0:
        S -= box
        cnt += 1
        last_box = box

while last_box + S not in boxes and S > 0:
    S -= 1

print(cnt, last_box + S)