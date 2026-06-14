with open(r'..\..\Files\26_4629.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

N = N // 4
data = sorted(data)[::-1]

customer = sum(data) - sum(data[:N]) // 2
sailor = sum(data) - sum(data[::-1][:N]) // 2

print(customer, sailor)