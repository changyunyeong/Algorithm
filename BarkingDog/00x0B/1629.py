import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
def fun(a,b,c):
    if b == 1: # base
        return a % c
    ans = fun(a, b//2, c) # 더 작게 거듭제곱 해야 메모리 이용 줄일 수 있음
    if (b%2 == 0):
        return ans * ans % c
    else:
        return ans * ans * a % c

print(fun(a,b,c))