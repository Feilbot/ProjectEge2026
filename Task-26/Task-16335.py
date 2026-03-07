with open(r'..\Files\26_16335.txt') as file:
    N = int(file.readline())
    layers = sorted(set(int(i) for i in file))[::-1]

last_layer = layers[0]
cnt = 1

for layer in layers:
    if last_layer - layer >= 4:
        last_layer = layer
        cnt += 1

print(cnt, last_layer)