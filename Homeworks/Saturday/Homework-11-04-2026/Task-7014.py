with open(r'../../../Files/26_7014.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

amount_of_butterflies = 1
ans = 0

max_price = max(prices)
max_cash = (len(prices) - prices[::-1].index(max_price)) * max_price

for price in prices:

    if price < max(prices):
        amount_of_butterflies += 1

    else:
        cash = amount_of_butterflies * price
        ans += cash
        amount_of_butterflies = 1

    prices = prices[1:]

print(ans, max_cash)