with open(r'..\..\..\..\Files\26_12113.txt') as file:
    N = file.readline()
    boxes = sorted(set([int(i) for i in file]))[::-1]

previous_box_chet = boxes[boxes.index([i for i in boxes if i % 2 == 0][0])]
ans_chet = 1

previous_box_nechet = boxes[boxes.index([i for i in boxes if i % 2 == 1][0])]
ans_nechet = 1

for box in boxes:

    if previous_box_chet - box >= 7 and box % 2 != previous_box_chet % 2:
        previous_box_chet = box
        ans_chet += 1

    if previous_box_nechet - box >= 7 and box % 2 != previous_box_nechet % 2:
        previous_box_nechet = box
        ans_nechet += 1

print(max(ans_chet, ans_nechet), max(previous_box_chet, previous_box_nechet))