with open(r'..\..\Files_P\24_8702.txt') as file:
    data = file.readline()

data = data.replace('.A', ' +')
data = data.split()

