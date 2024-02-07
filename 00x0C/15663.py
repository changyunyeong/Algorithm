n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
        
lst = []

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(len(arr)):
        if arr[i] not in lst:
            lst.append(arr[i])
            fun(i+1)
            lst.pop()
            
fun(0)