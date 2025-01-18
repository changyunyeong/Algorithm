l, c = map(int, input().split())
arr = sorted(list(map(str, input().split())))
con = ['a', 'e', 'i', 'o', 'u']
lst = []

def bfs(depth, idx):
    if len(lst) == l:
        vo, co = 0,0 # 모음, 자음
        
        for i in range(l):
            if lst[i] in con:
                vo += 1
            else:
                co += 1
        
        if vo >= 1 and co >= 2:
            print("".join(map(str, lst)))
    
    for i in range(idx, c):
        lst.append(arr[i])
        bfs(depth+1, i+1)
        lst.pop()

bfs(0,0)