# Формула Хартли
# N = 2 ** i | i = log2(N) , где N - мощность алфавита; i - вес в битах

# Формула объёма сообщения
# I = L * i, где I - объём сообщения, L - lenght (длинна)

# Task-1855
L = 101
N = 10 + 4090
i = 1 # bit
while 2**i < N:
    i += 1
I = (L * i / 8).__ceil__() # byte
print(I * 2048 / 1024)

# Task-23270
for L in range(1, 10 ** 6):
    N = 10 + 27
    # i = log2(N)
    i = 1 # bit
    while 2**i < N:
        i += 1
    I = (L * i / 8).__ceil__() # byte
    if I * 3548 > 12 * 1024:
        print(L)
        break

# Task-23195
for N in range(1, 10 ** 6):
    L = 172
    # i = log2(N)
    i = 1 # bit
    while 2**i < N:
        i += 1
    I = (L * i / 8).__ceil__() # byte
    if I * 356984 > 54 * 1024 * 1024:
        print(N)
        break