from math import dist
from itertools import combinations

def F(st1, st2):
    ans = []
    for s1 in st1:
        for s2 in st2:
            ans.append(dist(s1, s2))
    return ans

with open(r'..\Files\27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        i = i.replace(',', '.').split()
        dot = list(map(float, i[:2]))
        dots.append(dot)
        if i[2][1] != 'I' and int(i[2][1]) >= 8:
                stars.append(dot)

cluster_1 = [i for i in dots if i[0] > 22]
cluster_2 = [i for i in dots if i[0] < 22 and i[1] < 22]
cluster_3 = [i for i in dots if i[0] < 22 and i[1] > 22]

stars_1 = [i for i in stars if i in cluster_1]
stars_2 = [i for i in stars if i in cluster_2]
stars_3 = [i for i in stars if i in cluster_3]

stars = [stars_1, stars_2, stars_3]

B1 = F(stars_1, stars_2) + F(stars_2, stars_3) + F(stars_3, stars_1)
B1 = min(B1) * 10_000

B2 = [dist(s1, s2) for s in stars for s1, s2 in combinations(s, 2)]

B2 = sum(B2) / len(B2) * 10_000

print(int(B1), int(B2))