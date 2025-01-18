n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = []

def fun():
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(n):
        lst.append(arr[i])
        fun()
        lst.pop()
        
fun()