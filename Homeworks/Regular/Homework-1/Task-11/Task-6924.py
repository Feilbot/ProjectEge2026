alphabet = 10 + 4180 * 2 # 0-9 + строчные И прописные символы

i = 14
if 2 ** i >= alphabet:
    print(True)
# => i == 14 бит

one_user = 604 * 1024 * 8 / 2048
otvet = one_user / (14 * 8)
print(otvet.__ceil__())