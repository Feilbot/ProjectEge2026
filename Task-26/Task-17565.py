with open(r'..\Files\26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = [[sum(map(int, i.split()[1:4])), int(i.split()[4]), int(i.split()[0])] for i in file]

sailors = sorted(sailors, key=lambda x: (-x[0], -x[1], x[2]))

passed = sailors[:S]
rejected = sailors[S:]
half_score = passed[-1][0]

print([sailor[-1] for sailor in passed[::-1] if sailor[0] != half_score][0])
print(len([sailor for sailor in sailors if half_score == sailor[0]]))