n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += dfs(nx, ny)
    
    return cnt


result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

result.sort()

print(len(result))
for x in result:
    print(x)
