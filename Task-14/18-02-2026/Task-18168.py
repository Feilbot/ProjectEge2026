def convert(num, sys):
    num_sys = ''
    while num:
        num_sys += str(num % sys)
        num //= sys
    return num_sys[::-1]

ans = []

for x in range(10, 70_001):
    num = 5**2025 + 5**400 - x
    ans.append([convert(num, 5).count('4'), x])
print(max(ans)[1])