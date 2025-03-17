import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(arr, x, y):
    queue = deque()
    queue.append((x, y))
    extnt = 1
    arr[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
        
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                extnt += 1
            
    return extnt

paint = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            paint.append(bfs(arr, i, j))

print(0 if not paint else len(paint))
print(0 if not paint else max(paint))