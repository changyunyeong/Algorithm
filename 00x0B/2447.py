# 재귀는 n부터 생각할 것!
# function define -> base condition -> recursion
import sys
input = sys.stdin.readline

n = int(input())

def fun(n, i, j):
    if n == 1:
        return 