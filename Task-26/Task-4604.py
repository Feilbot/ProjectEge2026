with open(r'..\Files\26_4604.txt') as file:
    N = int(file.readline())
    boxes = sorted(set(int(i) for i in file))[::-1]

max_box = boxes[0]
cnt = 1

for box in boxes:
    if max_box - box >= 3:
        max_box = box
        cnt += 1

print(cnt, max_box)