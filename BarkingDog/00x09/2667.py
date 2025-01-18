from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(result, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(result, i, j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])