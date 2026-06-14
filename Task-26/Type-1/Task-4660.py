with open(r'../../Files/26_4660.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)

customer = data[::-1]
sailor = data

N = N // 4

print(sum(data) - sum(data[::-1][3::4]) // 2)

print(sum(sailor) - sum(sailor[:N]) / 2)