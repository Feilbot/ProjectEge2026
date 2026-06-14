with open(r'..\..\Files\26_4684.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

original_N = N
N = N // 6
data = sorted(data)

customer = 0
for x in range(0, (original_N - N * 6) + 1):
    customer = max(sum(data) - sum(data[x::6]) / 2, customer)

sailor = sum(data) - sum(data[:N]) / 2

print(customer, sailor)