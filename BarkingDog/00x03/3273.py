import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
x = int(input())

seen = set() # list를 이용하게 되면 O(n^2)
cnt = 0

for i in arr:
    if x-i in seen: # set의 경우 in 연산 O(1)
        cnt += 1
    seen.add(i)

print(cnt)