from re import finditer

with open(r'..\..\Files_P\24_8702.txt') as file:
    data = file.readline()

ans = []

for K in range(600, 900):
    pattern = fr'\.([.]*(A[A-Z]*)[.]*){K}\.'

    matches = [match.group() for match in finditer(pattern, data)]

    if not matches:
        ans.append(100_000)
    else:
        ans.append(len(min(matches, key=len)))

print(min(ans))