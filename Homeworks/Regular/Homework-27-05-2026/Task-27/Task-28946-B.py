from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_B_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [i for i in dots if i[0] > 24]
cluster_2 = [i for i in dots if i[0] < 24 and i[1] > 23]
cluster_3 = [i for i in dots if i[0] < 24 and i[1] < 23]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(len(cluster_1), len(cluster_2), len(cluster_3))

x = center_1[0]
y = center_1[1]
B1 = sum(1 for i in cluster_1 if x-0.9 < i[0] < x+0.9 and y-0.9 < i[1] < y+0.9)

B2 = (center_2[1] - center_3[1]) * 10_000

print(B1, int(B2))