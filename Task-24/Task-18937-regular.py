from re import finditer

with open(r'..\files\24_18937.txt') as file:
    data = file.readline()

num = r'([2-5][0-5]*|0)'
pattern = fr'({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))