import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def fun(n, r, c):
    if n == 0:
        return 0
    
    half = 2**(n-1)
    if (r < half and c < half): return fun(n-1, r, c)