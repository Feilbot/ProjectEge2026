from string import printable

for x in printable[:19]:
    num = int(fr'78{x}79643', 19) + int(fr'25{x}43', 19) + int(fr'63{x}5', 19)
    if num % 18 == 0:
        print(num / 18)
        break