from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'../Files/27_A_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]

cluster_1 = [i for i in dots if i[1] < 3]
cluster_2 = [i for i in dots if i[1] > 3]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

Px = (center_1[0] + center_2[0]) * 10_000 / 2
Py = (center_1[1] + center_2[1]) * 10_000 / 2

print(int(Px), int(Py))