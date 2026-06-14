from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'..\Files\27_B_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        i = i.replace(',', '.').split()
        dot = list(map(float, i[:2]))
        dots.append(dot)
        if i[2][0] == 'J':
            stars.append(dot)

cluster_1 = [i for i in dots if i[0] > 22]
cluster_2 = [i for i in dots if i[0] < 22 and i[1] < 22]
cluster_3 = [i for i in dots if i[0] < 22 and i[1] > 22]

stars_1 = [i for i in stars if i in cluster_1]
stars_2 = [i for i in stars if i in cluster_2]
stars_3 = [i for i in stars if i in cluster_3]

print(len(stars_1), len(stars_2), len(stars_3))

def F(cluster_1, cluster_2):
    ans = []
    for dot1 in cluster_1:
        for dot2 in cluster_2:
            ans.append(dist(dot1, dot2))
    return min(ans), max(ans)

B1 = min(F(stars_1, stars_2)[0], F(stars_2, stars_3)[0], F(stars_3, stars_1)[0]) * 10_000
B2 = max(F(stars_1, stars_2)[1], F(stars_2, stars_3)[1], F(stars_3, stars_1)[1]) * 10_000

print(int(B1), int(B2))