with open(r'Files\17 (1).txt') as file:
    data = file.readline()

pairs_1 = []
pairs_2 = []
pair = []
cnt = 0

ans = 0

max_2_num = 0
max_sum = 0

for num in data:
    if "\n" in num:
        num = num.replace("\n", "")
    if len(num) == 2:
        max_2_num = max(int(num), max_2_num)
    cnt += 1
    pair.append(num)
    if cnt == 2:
        pairs_1.append(pair)
        pair = []
        cnt = 0
for num in data[1:]:
    if "\n" in num:
        num = num.replace("\n", "")
    cnt += 1
    pair.append(num)
    if cnt == 2:
        pairs_2.append(pair)
        pair = []
        cnt = 0

for pair in pairs_1:
    summy = int(pair[0]) + int(pair[1])
    max_sum = max(max_sum, summy)
    if summy % max_2_num == 0:
        if len(pair[0]) == 2 or len(pair[1]) == 2:
            if len(pair[0]) != len(pair[1]):
                ans += 1
        else:
            ans += 1

for pair in pairs_2:
    summy = int(pair[0]) + int(pair[1])
    max_sum = max(max_sum, summy)
    if summy % max_2_num == 0:
        if len(pair[0]) == 2 or len(pair[1]) == 2:
            if len(pair[0]) != len(pair[1]):
                ans += 1
        else:
            ans += 1

print(ans, max_sum)