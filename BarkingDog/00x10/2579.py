import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * 301
for i in range(1, n+1):
    stair[i] = int(input())
    
d = [0] * 301
d[1] = stair[1]
d[2] = stair[1] + stair[2] # 최댓값을 구하는 문제이니 계단을 많이 밟는 게 유리 => 계단이 2개일 경우 반드시 둘 다 밟아야 함
d[3] = max(stair[1] + stair[3], stair[2] + stair[3])
# 1,2,3번째 계단을 모두 밟는 건 불가능하니 첫 번째 계단과 두 번째 계단 비교

for i in range(4, n+1):
    d[i] = max(stair[i] + stair[i-1] + d[i-3], stair[i] + d[i-2])

print(d[n])