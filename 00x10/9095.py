# 테이블 정의하기
# 점화식 찾기

import sys
input = sys.stdin.readline

d = [0] * 1000001
d[1] = 1
d[2] = 2
d[3] = 4

t = int(input())
for _ in range(t):
    n = int(input())
    
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    print(d[n])