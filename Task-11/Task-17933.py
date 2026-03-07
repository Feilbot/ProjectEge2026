symbols = 1231
amount = 523872
size = 432 #Мбайт
size_bit = size * 1024**2 * 8
print(2**(size_bit/amount/symbols).__floor__() + 1)
# + 1, т.к. получаем 5 степень с копейками