from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
dist = [0] * (f + 1) # 초기 배열 0
# dist = [0 for _ in range(f+1)]

def bfs():
    queue = deque() 
    queue.append(s) # 시작점
    dist[s] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == g:
            return dist[x] - 1
        
        else:
            for i in (x+u, x-d):
                if 0 < i <= f and dist[i] == 0:
                    dist[i] = dist[x] + 1
                    queue.append(i)
                    
    return "use the stairs"

print(bfs())