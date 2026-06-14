with open(r'..\..\Files\26_21910.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)[::-1]
ans = 1
previous_box = boxes[0]

for box in boxes[1:]:
    if previous_box - box >= 9:
        previous_box = box
        ans += 1

print(ans, previous_box)