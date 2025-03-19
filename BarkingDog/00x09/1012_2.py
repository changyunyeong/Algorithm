import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]
t = int(input().strip()) # tc

def bfs(arr, x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    
    while queue:
        x,y = queue.popleft() 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
    return


for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(arr, i, j)
                cnt += 1

    print(cnt)