n, m = map(int, input().split())
arr = []

def fun(cur):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
        
    for i in range(cur, n+1):
            arr.append(i)
            fun(i)
            arr.pop()
            
fun(1)