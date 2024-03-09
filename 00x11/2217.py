import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
arr.reverse()
ans = 0
for i in range(1, n+1):
    ans = max(ans, arr[i-1]*i)

print(ans)