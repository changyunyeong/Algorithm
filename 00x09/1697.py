from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n) # 시작점 추가
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            print(dist[x])
            break
        
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not dist[i]: # dist의 초기 배열은 0이기 때문에 항상 F
                dist[i] = dist[x] + 1
                queue.append(i)

MAX = 10 ** 5
dist = [0] * (MAX+1)
n, k = map(int, input().split())

bfs()