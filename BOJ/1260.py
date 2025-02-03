import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 인접 행렬

visited_bfs = [0]*(n+1) 
visited_dfs = visited_bfs.copy()

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited_dfs[i] == 0: # 방문 기록이 없는 노드 확인
            dfs(i) 

def bfs(v):
    queue = [v]
    visited_bfs[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)

from collections import defaultdict, deque
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 인접 리스트
    graph[b].append(a)

for key in graph:
    graph[key].sort() # 작은 숫자부터 방문
    
def dfs(v, visited):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            
            for next_node in reversed(graph[node]):
                if not visited[next_node]:
                    stack.append(next_node)

def bfs(v):
    queue = deque([v])
    visited = [False]*(n+1)
    visited[v] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

visited_dfs = [False]*(n+1)
dfs(v, visited_dfs)
print()
bfs(v)