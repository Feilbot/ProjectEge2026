with open(r'..\..\Files\26_17881.txt') as file:
    N = int(file.readline())
    failed_3 = []
    passed = []
    # file = ['4 4 4 4 4',
    #         '7 5 5 5 2',
    #         '10 3 4 4 5',
    #         '1 4 4 4 3',
    #         '6 3 5 5 3',
    #         '2 2 2 2 2',
    #         '13 2 2 2 3',
    #         '3 3 3 3 3']
    for i in file:
        i = list(map(int, i.split()))
        id = i[0]
        score = i[1:]
        info = [sum(score) / len(score), id]
        if score.count(2) == 3:
            failed_3.append(id)
        if 2 not in score:
            passed.append(info)

# N = 8

passed = sorted(passed, key=lambda x: (-x[0], x[1]))

failed_3 = sorted(failed_3)

print(passed[N//4 - 1][1], failed_3[0])
