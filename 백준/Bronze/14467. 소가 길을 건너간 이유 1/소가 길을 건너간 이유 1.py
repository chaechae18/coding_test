n = int(input())
count = 0

cow = [-1] * 11

for i in range(n):
    num, p = map(int, input().split())

    if cow[num] == -1:
        cow[num] = p
    else:
        if cow[num] != p:
            count += 1
            cow[num] = p
print(count)