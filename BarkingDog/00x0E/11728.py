import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []
idx1, idx2 = 0, 0

while idx1<len(a) and idx2<len(b):
    if a[idx1]<b[idx2]:
        arr.append(a[idx1])
        idx1 += 1
    else:
        arr.append(b[idx2])
        idx2 += 1
# 이 루프를 빠져나왔다면 어느 한 배열은 끝까지 다 돌았으므로 각 배열의 인덱스 비교
        
while idx1 < len(a):
    arr.append(a[idx1])
    idx1 += 1
    
while idx2 < len(b):
    arr.append(b[idx2])
    idx2 += 1
print(*arr)