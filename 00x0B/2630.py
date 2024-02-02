# 재귀는 n부터 생각할 것!
# function define -> base condition -> recursion
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = {0:0, 1:0}

def fun(row, col, n):
    cur = arr[row][col]
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if cur != arr[i][j]:
                k = n//2
                fun(row, col, k)
                fun(row, col+k, k)
                fun(row+k, col, k)
                fun(row+k, col+k, k)
                return
    
    result[cur] += 1
    return

fun(0,0,n)
for i in result.values():
    print(i)