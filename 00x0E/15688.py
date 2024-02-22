# import sys
# # input = sys.stdin.readline

# n = int(input())
# arr = [0] * 1000000

# for i in range(n):
#     a = int(input())
#     arr[a-1] += 1

# for i in range(1000000):
#     if arr[i] != 0:
#         for j in range(arr[i]):
#             print(i+1)

import sys
n=int(sys.stdin.readline())
tmp=[]
for i in range(n):
    tmp.append(int(sys.stdin.readline()))
for i in sorted(tmp):
    print(i)
# 파이썬은 10000인가 얼마 넘어가면 오류나서 안 되는 듯