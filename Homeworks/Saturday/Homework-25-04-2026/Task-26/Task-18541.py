with open(r'..\..\..\..\Files\26_18541.txt') as file:
    N, M = map(int, file.readline().split())
    data = [int(i) for i in file]

weights = sorted(data[:N])[::-1]
athletes = sorted(data[N:])[::-1]

lifted_weights = []
for athlete in athletes:
    for weight in weights:
        if athlete >= weight:
            lifted_weights.append(weight)
            break

print(sum(lifted_weights) / len(lifted_weights))
print(max(lifted_weights, key = lambda x: lifted_weights.count(x)))