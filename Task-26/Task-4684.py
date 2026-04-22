with open(r'..\Files\26_4684.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)

quarters = N // 6

one_bill = sum(products[:quarters]) // 2 + sum(products[quarters:])

some_bills = sum(products) - sum(products[::-1][5::6]) // 2

print(some_bills, one_bill)