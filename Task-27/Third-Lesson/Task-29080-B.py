from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

def F(st1, st2):
    ans = []
    for s1 in st1:
        for s2 in st2:
            ans.append(dist(s1, s2))
    return max(ans)

with open(r'..\Files\27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        i = i.replace(',', '.').split()
        dot = list(map(float, i[:2]))
        dots.append(dot)
        if i[2][0] == 'L':
            stars.append(dot)

cluster_1 = [i for i in dots if i[1] < 15]
cluster_2 = [i for i in dots if 15 < i[1] < 22]
cluster_3 = [i for i in dots if 22 < i[1]]

stars_1 = [i for i in stars if i in cluster_1]
stars_2 = [i for i in stars if i in cluster_2]
stars_3 = [i for i in stars if i in cluster_3]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(len(stars_1), len(stars_2), len(stars_3))

B1 = dist(center_1, center_3) * 10_000
B2 = max(F(stars_1, stars_2), F(stars_2, stars_3), F(stars_3, stars_1)) * 10_000

print(int(B1), int(B2))