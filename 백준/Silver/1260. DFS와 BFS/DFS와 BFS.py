from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(V)
print()

visited = [False] * (N+1)
queue = deque([V])
visited[V] = True

while queue:
    v = queue.popleft()
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
