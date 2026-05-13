with open(r'Files/17_9748.txt') as file:
    nums = [int(i) for i in file]

max_sum = 0
cnt = 0

checker = max(i for i in nums if str(i)[-2:] == '15')

for num1, num2, num3 in zip(nums, nums[1:], nums[2:]):
    if [len(str(i)) for i in [num1, num2, num3]].count(4) == 1:
        summ = num1 + num2 + num3
        if summ >= checker:
            cnt += 1
            max_sum = max(max_sum, summ)

print(cnt, max_sum)