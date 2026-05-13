with open(r'Files/17_4622.txt') as file:
    nums = [int(i) for i in file]

cnt = 0
max_sum = 0
checker = 0

for i in sorted(nums):
    if i > 0 and i % 19 == 0:
        checker = i
        break

for num1, num2 in zip(nums, nums[1:]):
    summ = num1 + num2
    if summ < checker:
        cnt += 1
        max_sum = max(max_sum, summ)

print(cnt, max_sum)