with open(r'..\Files\26_13394.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)[::-1]

sale_products = [i for i in products if i > 350]
new_N = len(sale_products)

k = 3

min_ans = sum(products) - sum((i*0.75).__floor__() for i in sale_products[k - 1::k])
max_ans = sum(products) - (sum(sale_products[- new_N // k:]) * 0.75).__floor__()

print(min_ans, max_ans)