num = 6*144**26 + 11*12**75 - 48
cnt = 0
while num :
    if num % 12 == int('b', 12):
        cnt += 1
    num //= 12
print(cnt)