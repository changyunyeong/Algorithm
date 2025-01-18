import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(range(1, n+1))

while (len(queue)) != 1: # 카드는 최소 두 개가 있어야 함
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())