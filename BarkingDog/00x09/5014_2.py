import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = list(map(int, input().split()))
# f층, 현재 s층, 목표 g층, up, down
arr = [0] * (f+1)

def bfs():
    queue = deque()
    queue.append(s)
    arr[s] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == g:
            print(arr[x]-1)
            return
        else:
            for i in (x-d, x+u):
                if 0 < i <= f and arr[i] == 0:
                    arr[i] = arr[x] + 1
                    queue.append(i)
        
    print("use the stairs")

bfs()