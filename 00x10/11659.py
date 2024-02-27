# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# for k in range(m):
#     sum = 0
#     i, j = map(int, input().split())
    
#     for l in range(i-1, j):
#         sum += arr[l]
    
#     print(sum)
## 시간 초과 ##

# i + (i+1) ... j == 1 + 2 + ... + j - (1 + 2 + ... i-1)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]
cnt = 0

for i in arr:
    cnt += i
    sum.append(cnt)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])
    
# 1. 누적 합 구하기: S[i] = S[i-1] + A[i]
# 2. 구간 합 구하기: S[j] - S[i-1]