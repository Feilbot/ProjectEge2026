def f(x, y, nums):
    if x > y:
        return 0
    elif x == y:
        if len(set(nums[1:])) > 50:
            return 1
        else:
            return 0
    else:
        return f(x + 2, y, nums + [x]) + f(x * 3, y, nums + [x]) + f(x * 4, y, nums + [x])

print(f(2, 400, []))