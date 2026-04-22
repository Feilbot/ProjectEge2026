with open(r'..\Files\26_4660.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)

quarters = N // 4

one_bill = sum(products[:quarters]) // 2 + sum(products[quarters:])

some_bills = sum(products) - sum(products[::-1][3::4]) // 2

print(some_bills, one_bill)