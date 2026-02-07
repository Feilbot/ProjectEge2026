with open(r'..\Files\24_23281.txt') as file:
    data = file.readline()

ans = 0

cnt_2025 = 0
cnt_Y = 0
counter = 0

data = data.replace('2025', '*')
for i in range(len(data)):
    if data[i] == '*':
        cnt_2025 += 1
    elif data[i] == 'Y':
        cnt_Y += 1
        if cnt_Y == 80 and cnt_2025 >= 90:
            ans = max(ans, cnt_Y + cnt_2025 + counter)
            cnt_2025, cnt_Y, counter = 0, 0, 0
    else:
        counter += 1
print(ans)

'''Текстовый файл состоит из 0-9 и A-Z. Определить max подряд символов последовательности, в которой кол-во 2025 >= 90 и кол-во Y = 80'''