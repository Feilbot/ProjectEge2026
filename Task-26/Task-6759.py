with open(r'..\Files\26_6759.txt') as file:
    N = int(file.readline())
    products = sorted(int(i) for i in file)[::-1]

triples = N // 3

min_ans = sum(products) - sum(products[:triples])

payed = sum(products) - sum(products[2::3])

print(min_ans, payed)