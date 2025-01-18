n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False]*n
lst = []

def fun(cur):
    if len(lst) == m:
        print(" ".join(map(str, lst)))
        return
    
    dup = 0
    for i in range(n):
        if not visited[i] and dup!=arr[i]:
            visited[i] = True
            lst.append(arr[i])
            dup = arr[i]
            fun(i+1)
            visited[i] = False
            lst.pop()
            
fun(0)