import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    
arr.sort(key = lambda a:(a[1], a[0]))

for i in arr:
    print(i[0], i[1])