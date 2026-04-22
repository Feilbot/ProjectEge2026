with open(r'..\Files\26_17687.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)[::-1]

k = 9

ans_min = sum(products[N//k:])

ans_max = sum(products) - sum(products[k - 1::k])

print(ans_min, ans_max)