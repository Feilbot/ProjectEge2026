from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_B_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        i = i.replace(',', '.').split()
        dot = list(map(float, i[:2]))
        dots.append(dot)
        if i[2][0] == 'Y':
            stars.append(dot)

cluster_1 = [i for i in dots if i[0] > 22]
cluster_2 = [i for i in dots if i[0] < 22 and i[1] > 22]
cluster_3 = [i for i in dots if i[0] < 22 and i[1] < 22]

stars_1 = [i for i in stars if i in cluster_1]
stars_2 = [i for i in stars if i in cluster_2]
stars_3 = [i for i in stars if i in cluster_3]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(len(stars_1), len(stars_2), len(stars_3))

B1 = dist(center_1, center_3) * 10_000

B2_1 = max(dist(dot, center_1) for dot in stars_1)
B2_2 = max(dist(dot, center_2) for dot in stars_2)
B2_3 = max(dist(dot, center_3) for dot in stars_3)

B2 = max(B2_1, B2_2, B2_3) * 10_000

print(int(B1), int(B2))