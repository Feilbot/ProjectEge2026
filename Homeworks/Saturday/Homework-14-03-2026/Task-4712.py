with open(r'..\..\..\Files\26_4712.txt') as file:
    N = file.readline()
    boxes = sorted(set(int(i) for i in file))[::-1]

previous_box = boxes[0]
ans = 1

for box in boxes:
    if previous_box - box >= 3:
        ans += 1
        previous_box = box

print(ans, previous_box)