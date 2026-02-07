a = [[12, 34], [13, 60]]

print(sorted(a, key = lambda x:(x[0], -x[1])))