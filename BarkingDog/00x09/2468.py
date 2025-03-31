import sys
from collections import deque
input = sys.stdin.readline

arr = []
n = int(input())    
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(r, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1 # 방문 노드 (기존과 다르게 배열을 새로 만들어야 함함)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i]
            
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            
            if visited[nx][ny] == 0 and arr[nx][ny] > r:
                visited[nx][ny] = 1
                queue.append((nx, ny))

max_h = max(map(max, arr))
ans = 1
for r in range(max_h+1):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] > r and visited[i][j] == 0:
                bfs(r, i, j, visited)
                cnt += 1
    ans = max(ans, cnt)

print(ans)