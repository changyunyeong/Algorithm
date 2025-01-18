# 재귀는 n부터 생각할 것!
# function define -> base condition -> recursion
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = {-1:0, 0:0, 1:0} # 딕셔너리, -1,0,1 tp rodml zl

def fun(row, col, n):
    cur = arr[row][col] # 종이의 시작
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if arr[i][j] != cur:
                k = n//3 # 9 -> 3 -> 1
                # 분할정복
                # 00 -> 01 -> 02 -> 10 -> 11 -> 12
                fun(row, col, k)
                fun(row, col+k, k)
                fun(row, col+(k*2), k)
                fun(row+k, col, k)
                fun(row+k, col+k, k)
                fun(row+k, col+(k*2), k)
                fun(row+(k*2), col, k)
                fun(row+(k*2), col+k, k)
                fun(row+(k*2), col+(k*2), k)
                return
    
    result[cur] += 1
    return

fun(0,0,n)
for i in result.values():
    print(i)
            