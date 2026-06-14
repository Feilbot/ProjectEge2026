from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append([float(x), float(y)])

cluster_1 = [i for i in dots if i[1] < 10]
cluster_2 = [i for i in dots if i[1] > 10]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(len(cluster_1), len(cluster_2)) # => в 1 кластере меньше точек, а во втором - больше

A1 = min(dist(center_2, s) for s in stars) * 10_000
A2 = max(dist(center_2, s) for s in stars) * 10_000

print(int(A1), int(A2))