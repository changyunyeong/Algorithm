from collections import deque

n, m = map(int, input().split())
graph = []

dx = [1,0,-1,0]
dy = [0,1,0,-1] # 상하좌우

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문했단 걸 0으로 표시 (0이면 방문 안 하기 때문)
                queue.append((nx, ny))
                cnt += 1 # 그림 크기 1 증가
                
    return cnt

paint = [] # 그림 크기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))
            
if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))