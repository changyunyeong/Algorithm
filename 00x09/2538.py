from collections import deque

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
# graph = []
dx = [1,0,-1,0] # 세로
dy = [0,1,0,-1] # 가로

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    # graph[a][b] == 0/---
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1 # 색칠된 칸
                queue.append((nx, ny))
                cnt += 1
                
    return cnt

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1
    # for i in range(y1, y2):  # x와 y가 바뀌어야 합니다.
    #     for j in range(x1, x2):  # x와 y가 바뀌어야 합니다.
    #         graph[i][j] += 1

maze = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0: # 색칠되지 않은 칸이 있으면
            graph[i][j] += 1 # 넓이 추가
            maze.append(bfs(i, j))

print(len(maze))
print(*sorted(maze))

# [세로][가로] [y][x]