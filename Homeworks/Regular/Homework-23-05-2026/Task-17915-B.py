from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'Files/27_B_17915.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [i for i in dots if i[0] < 15 and i[1] > 15]
cluster_2 = [i for i in dots if i[0] > 15 and i[1] > 15]
cluster_3 = [i for i in dots if i[0] < 15 and i[1] < 15]
cluster_4 = [i for i in dots if i[0] > 15 and i[1] < 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)
center_4 = center(cluster_4)

Px = (center_1[0] + center_2[0] + center_3[0] + center_4[0]) * 10_000 / 4
Py = (center_1[1] + center_2[1] + center_3[1] + center_4[1]) * 10_000 / 4

print(int(Px), int(Py))