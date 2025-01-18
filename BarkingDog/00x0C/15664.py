n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = []
visited = [False]*n

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    dup = 0
    for i in range(cur, n):
        if not visited[i] and dup!=arr[i]:
            visited[i] = True
            dup = arr[i]
            lst.append(arr[i])
            fun(i+1)
            visited[i] = False
            lst.pop()
            
fun(0)