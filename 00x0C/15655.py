n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(cur, n):
        if arr[i] not in lst:
            lst.append(arr[i])
            fun(i+1)
            lst.pop()     

fun(0)