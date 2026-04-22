from string import printable

with open(r'24_7688.txt') as file:
    data = file.readline().upper()

data = data.replace('TXA', '***')
data = data.replace('XA', '**')
data = data.replace('XY', '**')

for i in printable[:36]:
    data = data.replace(i.upper(), '!')

data = data.split('!')

print(len(max(data, key=len)))