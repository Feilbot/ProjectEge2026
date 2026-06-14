with open(r'..\..\Files\26_21719.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)

students = {}

for i in data:
    if i[0] not in students:
        students[i[0]] = [i[1]]
    else:
        if i[1] not in students[i[0]]:
            students[i[0]] += [i[1]]

ans = 0
good_students = []

for student in students:
    tasks = students[student]
    if len(tasks) > 1:
        alternation = 1
        for task1, task2 in zip(tasks, tasks[1:]):
            if task2 - task1 == 2:
                alternation += 1
            else:
                ans = max(ans, alternation)
                good_students.append([student, ans])
                alternation = 1

for i in good_students:
    if i[1] == ans:
        print(i[0], ans)
        break