import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 10 ** 5
visited = [0] * (MAX + 1) 

def bfs():
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            print(visited[x])
            break
            
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

bfs()