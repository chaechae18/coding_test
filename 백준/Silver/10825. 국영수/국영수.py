n = int(input())
stu = []

for i in range(n):
    name, korean, english, math = input().split()
    stu.append((name, int(korean), int(english), int(math)))

def sorts(x):
    return (-x[1], x[2], -x[3], x[0])

stu.sort(key=sorts)

for student in stu:
    print(student[0])