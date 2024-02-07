n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def fun():
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    for i in arr:
        if i not in lst:
            lst.append(i)
            fun()
            lst.pop()
        
fun()