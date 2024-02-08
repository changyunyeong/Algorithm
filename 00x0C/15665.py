n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
arr = sorted(list(set(map(int, input().split()))))
lst = []

def fun():
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    for i in arr:
        lst.append(i)
        fun()
        lst.pop()
        
fun()