n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0

def dfs(x):
    global cnt
    visited[x] = True
    
    for i in graph[x]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(1)

print(cnt)