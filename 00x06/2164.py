import sys

n = int(sys.stdin.readline())
queue = list(range(1, n+1))

while (len(queue)) > 0:
    temp = queue.pop()
    queue.append(temp)

print(queue.pop())