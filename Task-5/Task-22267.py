def convert(sys, num):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for N in range(1, 100_000):
    n = convert(7, N)
    if n[-1] == '2':
        n = n.replace('1', '*')
        n = n.replace('3', '1')
        n = '21'+ n.replace('*', '3')
    else:
        n = '1' + n[1:] + '36'
    R = int(n, 7)
    if R < 744:
        ans.append([R, N])

ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0][1])

# answer = []
# max_R = max(ans)[0]
# for i in ans:
#     if i[0] == max_R:
#         answer.append(i[1])
# print(min(answer))