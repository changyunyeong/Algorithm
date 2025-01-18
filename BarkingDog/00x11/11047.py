import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
ans = 0
for i in range(n):
    arr.append(int(input()))
    
arr.reverse()
for i in range(n):
    ans += k // arr[i]
    k = k % arr[i]

print(ans)