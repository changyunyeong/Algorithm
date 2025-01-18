import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
d = [0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w,v))

for item in arr:
    w, v = item
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w]+v)
        
print(d[-1])