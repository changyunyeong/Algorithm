import sys
input = sys.stdin.readline

def fun(depth, idx):
    if depth == 6:
        print(" ".join(map(str, lst)))
        return
    
    for i in range(idx, k):
        # if arr[i] not in lst:
            lst.append(s[i])
            fun(depth+1, i+1)
            lst.pop()


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    lst = []
    fun(0,0)
    if k == 0:
        exit()
    print()