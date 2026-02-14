with open(r'..\..\..\Files\24_24895.txt') as file:
    data = file.readline()

data = data.replace('+', '*')
data = data.split('*')

ans = 0
numbers, signs_counter, num_counter = '', -1, 0
for num in data:
    if num != '':
        numbers += num
        signs_counter += 1
    else:
        ans = max(ans, len(numbers) + signs_counter)
        # print('numbers:', numbers, 'len:', len(numbers), 'signs:', signs_counter, 'ans:', ans)
        numbers, signs_counter, num_counter = '', -1, 0
    if num_counter > 40:
        ans = max(ans, len(numbers) + signs_counter)
        # print('numbers:', numbers, 'len:', len(numbers), 'signs:', signs_counter, 'ans:', ans)
        numbers, signs_counter, num_counter = '', -1, 0


print(ans)