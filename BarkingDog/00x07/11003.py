import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
dq = deque()

for i in range(n):
    
    while dq and (dq[-1][1] > a[i]): # dq의 원소가 있고 && dq에 들어오는 값이 dq 끝값보다 큰 원소가 있다면 
        dq.pop()
     
    dq.append((i + 1, a[i])) # 원소 삽입 (idx, val)
    
    if dq[-1][0] - dq[0][0] >= l: # index를 벗어나는 경우
        dq.popleft()
    
    print(dq[0][1], end=' ')
    
 # dq[-1][0]은 인덱스, dq[-1][1]은 값