# 재귀는 n부터 생각할 것!
# function define -> base condition -> recursion
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
    
def fun(row, col, n):
    cur = arr[row][col]
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if cur != arr[i][j]:
                k = n//2
                print('(', end="")
                fun(row, col, k)
                fun(row, col+k, k)
                fun(row+k, col, k)
                fun(row+k, col+k, k)
                print(')', end="")
                return
    
    if cur == 1:
        print(1, end="")
    else:
        print(0, end="")
    
    return

fun(0,0,n)
