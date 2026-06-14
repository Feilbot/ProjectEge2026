from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        i = i.replace(',', '.').split()
        dot = list(map(float, i[:2]))
        dots.append(dot)
        if i[2][:2] == 'L3':
            stars.append(dot)

cluster_1 = [i for i in dots if i[1] < 8]
cluster_2 = [i for i in dots if i[1] > 8]

stars_1 = [i for i in stars if i in cluster_1]
stars_2 = [i for i in stars if i in cluster_2]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(len(cluster_1), len(cluster_2))

A1 = max(dist(dot, center_2) for dot in stars) * 10_000
A2 = max(dist(dot, center_1) for dot in stars) * 10_000

print(int(A1), int(A2))