with open(r'../../../Files/26_20161.txt') as file:
    N = int(file.readline())
    prices = [list(map(int, i.split())) for i in file]

