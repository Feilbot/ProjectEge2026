from math import dist
from itertools import combinations

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append([float(x), float(y)])

cluster_1 = [i for i in dots if i[1] > 22]
cluster_2 = [i for i in dots if 16 < i[1] < 22]
cluster_3 = [i for i in dots if i[1] < 16]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

cluster_stars_1 = [i for i in stars if i in cluster_1]
cluster_stars_2 = [i for i in stars if i in cluster_2]
cluster_stars_3 = [i for i in stars if i in cluster_3]

B1_1 = min(dist(s1, s2) for s1, s2 in combinations(cluster_stars_1, 2))
B1_3 = min(dist(s1, s2) for s1, s2 in combinations(cluster_stars_3, 2))

print(len(cluster_stars_1), len(cluster_stars_2), len(cluster_stars_3))

B1 = min(B1_1, B1_3) * 10_000
B2 = dist(center_2, center_3) * 10_000

print(int(B1), int(B2))