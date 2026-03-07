from string import printable

ans = 0
ans_ANSWER = []

for x in range(0, 38):
    if x != 37:
        x = printable[x]
    else:
        x = printable[62+x%37]
    num_1 = f'C59{x}BA98F'[::-1]
    num_1_10 = 0
    for i in range(0, len(num_1)):
        if num_1[i] != '!':
            num_1_10 += int(num_1[i], 36) * 37**i
        else:
            num_1_10 += 36 * 37 ** i
    num_2 = f'E3{x}5DA9C6'[::-1]
    num_2_10 = 0
    for i in range(0, len(num_2)):
        if num_2[i] != '!':
            num_2_10 += int(num_2[i], 36) * 37**i
        else:
            num_2_10 += 36 * 37 ** i
    if (num_1_10 * num_2_10) % 36 == 0:
        num_ans = f'2{x}1'[::-1]
        for i in range(0, len(num_ans)):
            if num_ans[i] != '!':
                ans += int(num_ans[i], 36) * 37**i
            else:
                ans += 36 * 37 ** i
        ans_ANSWER.append(ans)
        ans = 0
print(max(ans_ANSWER))