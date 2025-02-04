import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip()))) # 개행 문자 제거

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] # 방향 확인 

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
        
            if graph[nx][ny] == 1: # 이동할 수 있으면 (방문한 노드는 거리 값이 업데이트 되므로 걸러짐)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            
    return graph[n-1][m-1]

print(bfs(0, 0))