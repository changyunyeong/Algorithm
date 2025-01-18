import sys
input = sys.stdin.readline

t = int(input())

d = [0]*100001
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2


for _ in range(t):
    n = int(input())
    
    if n >= 6:
        for i in range(6, n+1):
            d[i] = d[i-1] + d[i-5]
    
    print(d[n])