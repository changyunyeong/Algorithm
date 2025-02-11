import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
deq = deque(range(1, n+1))
cnt = 0

for i in arr:
    
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq)/2: # x.index(item) : 문자열 또는 리스트에 item이 몇 번째 인덱스에 처음 있는지 반환
                deq.append(deq.popleft())
                cnt += 1
            else:
                deq.appendleft(deq.pop())
                cnt += 1
print(cnt)