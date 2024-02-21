import sys
input = sys.stdin.readline

n = int(input())
arr = []
tmp = [0] * n
for _ in range(n):
    arr.append(int(input()))
    
def merge(start, end):
    mid = (start+end)//2
    idx1 = start
    idx2 = mid

    for i in range(start, end):
        if idx2 == end:  # 두 번째 배열을 다 돌면
            tmp[i] = arr[idx1]
            idx1 += 1 # 첫 번째 배열의 인덱스 증가
        elif idx1 == mid: # 첫 번째 배열을 다 돌면
            tmp[i] = arr[idx2]
            idx2 += 1 # 두 번째 배열의 인덱스 증가
        elif arr[idx1] <= arr[idx2]:
            tmp[i] = arr[idx1]
            idx1 += 1
        else:
            tmp[i] = arr[idx2]
            idx2 += 1

    for i in range(start, end):
        arr[i] = tmp[i]

def mergeSort(start, end):
    if (end == start + 1):
        return
    mid = (start+end)//2
    mergeSort(start, mid)
    mergeSort(mid, end)
    merge(start, end)

mergeSort(0, n)
for i in range(n):
    print(arr[i])        