n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = []

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(cur, n):
        lst.append(arr[i])
        fun(i)
        lst.pop()
        
fun(0)