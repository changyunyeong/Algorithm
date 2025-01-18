# 재귀는 n부터 생각할 것!
# n-1개의 원판을 옮길 수 있다 -> n개의 원판을 옮길 수 있다
# function define -> base condition -> recursion

n = int(input())

def fun(a, b, n): # 시작, 도착
    if n == 1:
        print(a, b)
        return
    # 막대 번호의 합 6
    fun(a, 6-a-b, n-1) # a -> 6-a-b
    print(a, b) # a -> b
    fun(6-a-b, b, n-1)

print(2**n-1)
fun(1,3,n)