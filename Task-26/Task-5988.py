with open(r'..\Files\26_5988.txt') as file:
    N = file.readline()
    boxes = sorted([[int(i.split()[0]), i.split()[1]] for i in file])[::-1]

previous_box_R = max(boxes, key=lambda x: (x[1] == 'R', x[0]))
previous_box_G = max(boxes, key=lambda x: (x[1] == 'G', x[0]))
previous_box_B = max(boxes, key=lambda x: (x[1] == 'B', x[0]))

max_amount_of_box_R = 1
max_amount_of_box_G = 1
max_amount_of_box_B = 1

for box in boxes:
    if previous_box_R[0] - box[0] >= 7 and previous_box_R[1] != box[1]:
        max_amount_of_box_R += 1
        previous_box_R = box
    if previous_box_G[0] - box[0] >= 7 and previous_box_G[1] != box[1]:
        max_amount_of_box_G += 1
        previous_box_G = box
    if previous_box_B[0] - box[0] >= 7 and previous_box_B[1] != box[1]:
        max_amount_of_box_B += 1
        previous_box_B = box

print(max(max_amount_of_box_R, max_amount_of_box_G, max_amount_of_box_B),
      max(previous_box_R[0], previous_box_G[0], previous_box_B[0]))