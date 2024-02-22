import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
temp = [0] * n

def merge(st, end):
    mid = (st+end)//2
    idx1 = st
    idx2 = mid
    
    for i in range(st, end):
        if idx1 == mid:
            temp[i] = arr[idx2]
            idx2 += 1
        elif idx2 == end:
            temp[i] = arr[idx1]
            idx1 += 1
        elif arr[idx1] <= arr[idx2]:
            temp[i] = arr[idx2]
            idx2 += 1
        else:
            temp[i] = arr[idx1]
            idx1 += 1
    
    for i in range(st, end):
        arr[i] = temp[i]
        
def mergeSort(st, end):
    mid = (st+end)//2
    
    if (end == st + 1):
        return
    
    mergeSort(st, mid)
    mergeSort(mid, end)
    merge(st, end)

mergeSort(0, n)
for i in range(n):
    print(arr[i])