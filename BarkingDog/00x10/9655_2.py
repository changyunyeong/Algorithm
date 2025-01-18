import sys
input = sys.stdin.readline

n = int(input())
d = [-1] * 1001
d[1] = 1
d[2] = 0
d[3] = 1

for i in range(4, n+1):
    if d[i-1] == 1 or d[i-3] == 1:
        d[i] = 0
    else:
        d[i] = 1

if d[n] == 1:
    print("SK")
else:
    print("CY")