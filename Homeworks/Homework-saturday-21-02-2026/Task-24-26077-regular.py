from re import finditer

with open(r'..\..\Files\24_26077.txt') as file:
    data = file.readline()

pattern = r'G([^G13579]*[13579]){45}[^G13579]*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))