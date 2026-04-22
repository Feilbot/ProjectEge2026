from re import finditer

with open(r'Files\24 (1).txt') as file:
    data = file.readline()

# ПРОВЕРКА РЫЗНЫХ ЗНАЧЕНИЙ

pattern = r'([A-Y]*[Z]){270}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){271}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){272}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){273}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){274}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){275}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){276}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){277}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){278}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){279}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))
pattern = r'([A-Y]*[Z]){280}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key = len)))