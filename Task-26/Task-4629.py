with open(r'..\Files\26_4629.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)

quarters = N // 4

min_ans = sum([product // 2 for product in products[::-1]][:quarters]) + sum([product for product in products[::-1]][quarters:])
max_ans = sum([product // 2 for product in products][:quarters]) + sum([product for product in products][quarters:])

print(min_ans, max_ans)