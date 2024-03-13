import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
d = [0] * 100001
for i in range(1, n+1):
    d[i] = d[i-1] + p[i-1]
    
### or ###
ans = 0
for i in range(1, n+1):
    ans += sum(p[:i])
print(ans)

# print(sum(d))
# 1 => 1+2 => 1+2+3