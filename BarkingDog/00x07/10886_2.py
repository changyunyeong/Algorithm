import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push_front':
        arr.appendleft(command[1])
    elif command[0] == 'push_back':
        arr.append(command[1])
    elif command[0] == 'pop_front':
        print(arr.popleft() if arr else -1)
    elif command[0] == 'pop_back':
        print(arr.pop() if arr else -1)
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        print(1 if not arr else 0)
    elif command[0] == 'front':
        print(arr[0] if arr else -1)
    elif command[0] == 'back':
        print(arr[-1] if arr else -1)