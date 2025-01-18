import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))
cnt = {} # 딕셔너리
idx = 1

for i in arr:
    if i in cnt:
        cnt[i][0] += 1
    else:
        cnt[i] = [1, idx] # 새로운 키 생성
        idx += 1

number = [[i, j] for i, j in cnt.items()] # 딕셔너리 쌍을 리스트 형태로 반환하여 리스트에 저장
number.sort(key = lambda x: (-x[1][0], x[1][1])) # 내림차순 정렬
result = []
for i, j in number:
    result += [i]*j[0] # 정렬된 순서대로 저장
    
print(*result)