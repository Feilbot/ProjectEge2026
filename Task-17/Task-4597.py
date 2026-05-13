with open(r'Files/17_4597.txt') as file:
    nums = [int(i) for i in file]

min_num = min(nums)
max_pair = 0
cnt = 0

for num1, num2 in zip(nums, nums[1:]):
    if num1 % 117 == min_num or num2 % 117 == min_num:
        cnt += 1
        max_pair = max(max_pair, num1 + num2)

print(cnt, max_pair)