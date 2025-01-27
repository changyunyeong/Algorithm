import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        arr.append(command[1])
    elif command[0] == 'pop':
        print(arr.pop() if arr else -1) # 스택이 비어있지 않으면 pop
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        print(1 if not arr else 0)
    elif command[0] == 'top':
        print(arr[-1] if arr else -1)
        
# 여러 줄 한꺼번에 입력 -> input, 공백으로 구분된 값 처리 -> list