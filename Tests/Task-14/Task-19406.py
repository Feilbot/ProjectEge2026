from string import printable

ans = 0

for x in printable[:35]:

    num = str(int(fr'6{x}QR{x}', 35) + int(fr'{x}59SH', 35) + int(fr'PH{x}69YW', 35))

    counter_list = []

    for number in sorted(set(num)):
        counter_list.append([num.count(number), int(number)])

    often_number = max(counter_list)[1]

    if int(num) % often_number**2 == 0:
        ans = int(num) // often_number**2

print(ans)