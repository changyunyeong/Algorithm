from collections import deque

m, n= map(int, input().split())
tom = []
queue = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    tom.append(list(map(int, input().split())))
    
for i in range (n):
    for j in range(m):
        if tom[i][j] == 1: # 시작 위치 저장
            queue.append((i,j))

while queue:
    x, y = queue.popleft() # 시작점
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if n > nx >= 0 and m > ny >= 0:
            if tom[nx][ny] == 0:
                tom[nx][ny] = tom[x][y] + 1 # 한 칸 이동
                queue.append((nx, ny))
cnt = 0
for i in tom:
    for j in i:
        if j == 0:
            print(-1)
            break
    cnt = max(cnt, max(i))
print(cnt-1)