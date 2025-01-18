from collections import deque

n, m = map(int, input().split())
maze = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    maze.append(list(map(int, input())))
    
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 이 노드는 현재 노드의 거리 + 1
                queue.append((nx, ny)) # 이 노드를 현재 노드로 전환
                
    return maze[n-1][m-1]

print(bfs(0,0))




# queue = deque() : 먼저 덱(deque)를 생성합니다. 덱은 양 끝에서 데이터를 넣고 뺄 수 있는 자료구조로, BFS에서는 방문할 노드를 저장하는 데 사용됩니다.
# queue.append((x,y)) : 시작 좌표를 덱에 추가합니다.
# while queue: : 덱이 비어 있지 않은 동안 계속 반복합니다. 덱이 비어 있다는 것은 더 이상 방문할 노드가 없다는 뜻이므로, 이 때 반복을 종료합니다.
# x, y = queue.popleft() : 덱에서 가장 먼저 들어온 노드를 꺼냅니다. 이 노드는 현재 방문하고 있는 노드입니다.
# for i in range(4): : 현재 노드의 상하좌우를 차례대로 확인합니다.
# nx = x + dx[i], ny = y + dy[i] : 확인할 노드의 좌표를 계산합니다.
# if nx < 0 or ny < 0 or nx >= n or ny >= m: : 계산한 좌표가 미로의 범위를 벗어나면 이 노드는 무시하고 다음 노드를 확인합니다.
# if maze[nx][ny] == 1: : 계산한 좌표의 노드가 아직 방문하지 않은 노드라면,
# maze[nx][ny] = maze[x][y] + 1 : 이 노드는 현재 노드의 거리 + 1만큼 떨어져 있습니다. 이 값을 해당 노드에 저장합니다.
# queue.append((nx, ny)) : 이후 이 노드를 방문하기 위해 덱에 추가합니다.
# return maze[n - 1][m - 1] : 모든 노드를 방문한 후, 도착지의 거리를 반환합니다. 이 값이 시작지에서 도착지까지의 최단 거리입니다.