from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [i for i in dots if i[1] < 15]
cluster_2 = [i for i in dots if i[1] > 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(len(cluster_1), len(cluster_2)) # => кластере 2 больше точек

A1 = sum(1 for i in cluster_2 if i[1] < center_2[1])
A2 = abs(center_1[0] - center_2[0]) * 10_000

print(A1, int(A2))