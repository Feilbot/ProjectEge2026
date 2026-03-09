with open(r'../../../Files/24_26078.txt') as file:
    data = file.readline()

data = data.split('W')

ans = 0

for i in range(len(data) - 89):
    line = data[i:i+90]
    if '' not in line:
        counter_2025 = 0
        for subline in line:
            counter_2025 += subline.count('2025')
        if counter_2025 >= 110:
            ans = max(ans, len('W'.join(line)))

print(ans)