n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
lst = []
# visited = [False]*n

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(cur, len(arr)):
        # if i not in lst:
            lst.append(arr[i])
            fun(i)
            lst.pop()

fun(0)