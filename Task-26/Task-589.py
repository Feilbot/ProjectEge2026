with open(r'..\Files\26_589.txt') as file:
    N = file.readline()
    prices = sorted(int(i) for i in file)

k = 2
ans = 0
max_price_on_sale = 0

for x in range(0, max(prices)//500 + 1):
    group = [i for i in prices if x * 500 < i <= (x + 1) * 500]
    N = len(group)
    if N > 1:
        ans += sum(i / k for i in group[:N//k])
        max_price_on_sale = max(max_price_on_sale, max(group[:N // k]))

print(int(ans), int(max_price_on_sale / 2))