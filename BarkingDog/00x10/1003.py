import sys
input = sys.stdin.readline

t = int(input())
d = [0]*41
d[0] = 0
d[1] = 1

for _ in range(t):
    n = int(input())
    
    for i in range(2, n+1):
        d[i] = d[i-1]+d[i-2]
    
    if n == 0: # 항상 예외를 조심하자
        print(1, 0)
    else:
        print(d[n-1], d[n])