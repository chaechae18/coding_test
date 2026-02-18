m = int(input())
p = list(map(int, input().split()))


bm = m
bs = 0

for x in p:
    if bm >= x:
        s = bm // x
        bs += s
        bm -= s * x

b = bm + bs * p[-1]



tm = m
ts = 0

for i in range(3, len(p)):
    if p[i-3] > p[i-2] > p[i-1]:  
        s = tm // p[i]
        ts += s
        tm -= s * p[i]
    
    elif p[i-3] < p[i-2] < p[i-1]: 
        tm += ts * p[i]
        ts = 0

t = tm + ts * p[-1]


if b > t:
    print("BNP")
elif b < t:
    print("TIMING")
else:
    print("SAMESAME")