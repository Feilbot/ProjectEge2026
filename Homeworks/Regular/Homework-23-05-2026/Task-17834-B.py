from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'Files/27_B_17834.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [i for i in dots if (i[0] < 4 and i[1] > 3) or (i[0] <= 3 and i[1] > 2) or (i[0] < 1 and i[1] > 1)]
cluster_2 = [i for i in dots if (0 < i[0] < 8 and i[1] < 2) or (3 < i[0] < 5 and i[1] < 3)]
cluster_3 = [i for i in dots if (i[0] > 5 and i[1] > 2) or (4 < i[0] <= 5 and i[1] > 4)]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

Px = (center_1[0] + center_2[0] + center_3[0]) * 100 / 3
Py = (center_1[1] + center_2[1] + center_3[1]) * 100 / 3

print(int(Px), int(Py))