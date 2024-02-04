import sys
input = sys.stdin.readline

n = int(input())
star = [[' ']*2*n for _ in range(n)]

def fun(row, col, n):
    
    if n == 3:
        star[row][col] = '*'
        star[row+1][col-1] = star[row+1][col+1] = '*'
        for i in range(-2, 3):
            star[row+2][col+i] = '*'
            
    else:
        ans = n//2
        fun(row, col, ans)
        fun(row+ans, col-ans, ans)
        fun(row+ans, col+ans, ans)

fun(0, n-1, n)
for i in star:
    print("".join(i))
    
# 규칙 찾는 게 제일 어려웠다