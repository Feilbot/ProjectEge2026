with open(r'../../Files/26_4604.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(set(data))

max_ln = 0
max_mini_box = 0

for x in range(0, 10):
    ln = 0
    previous = 0
    for i in data[x:]:
        if i - previous >= 3:
            ln += 1
            previous = i
    max_ln = max(max_ln, ln)
    if max_ln == ln:
        max_mini_box = data[x:][0]
print(max_ln, max_mini_box)