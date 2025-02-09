import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(1, n+1))
temp = []
idx = 0

for i in range(n):
    idx += k - 1
    idx %= len(arr) 
    temp.append(arr.pop(idx))  

print("<", ", ".join(map(str, temp)), ">", sep='')