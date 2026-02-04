with open(r'..\Files\24_11241.txt') as file:
    data = file.readline()

ans = 0
cnt = 0

for i in data:
    if i not in 'ABCD':
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0
ans = max(cnt, ans)
print(ans)