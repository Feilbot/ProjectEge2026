a = '1234567898543345'

for i in range(0, len(a)):
    a = a[:(-1*i)]
    print(a)