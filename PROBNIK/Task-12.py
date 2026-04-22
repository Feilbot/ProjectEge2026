num = bin(135)[2:]
num = num.replace('0', '2')
num = num.replace('1', '0')
num = num.replace('2', '1')

print(int(num, 2))