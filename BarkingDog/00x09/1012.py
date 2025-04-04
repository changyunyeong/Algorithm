from collections import deque

t = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # nx >= m 이라고 써서 15번 넘게 저지랄 했다...
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)