from re import finditer

with open(r'..\..\Files_P\24_8834.txt') as file:
    data = file.readline()

pattern = r'A(( |[B-Z])*A){97}( |[B-Z])*\.'
pattern = r'(A[^A.]*){98}\.'

matches = [match.group() for match in finditer(pattern, data)]

print(len(min(matches, key = len)))