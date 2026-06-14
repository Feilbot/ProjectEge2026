def simple_dividers(num):
    dividers = []

    if num % 2 == 0:
        dividers.append(2)
        while num % 2 == 0:
            num //= 2

    d = 3
    while d ** 2 <= num:
        if num % d == 0:
            dividers.append(d)
            while num % d == 0:
                num //= d
        d += 2
    if num > 1:
        dividers.append(num)

    return dividers

def results(start, main_divider, remainder, limit=None):
    found = []
    num = start + 1
    count = 0
    while limit is None or count < limit:
        dividers = simple_dividers(num)
        if len(dividers) >= 2:
            M = min(dividers) + max(dividers)
            if M % main_divider == remainder:
                found.append((num, M))
                count += 1
        num += 1
    return found

results = results(23_600_000, 213, 171, limit=6)

for num, M in results:
    print(num, M)