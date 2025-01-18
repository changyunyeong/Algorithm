import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
temp = [0]*n

def merge(st, end):
    mid = (st+end)//2
    idx1 = st
    idx2 = mid
    
    for i in range(st, end):
        if mid == idx1:
            temp[i] = arr[idx2]
            idx2 += 1
        elif end == idx2:
            temp[i] = arr[idx1]
            idx1 += 1
        elif arr[idx1] <= arr[idx2]:
            temp[i] = idx1
            idx1 += 1
        else:
            temp[i] = idx2
            idx2 += 1
    
    for i in range(st, end):
        arr[i] = temp[i]
        
def mergeSort(st, end):
    mid = (st+end)//2
    mergeSort(st, mid)
    mergeSort(mid, end)
    merge(st, end)

mergeSort(0, n)
print(*arr)