import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x:(x[1], x[0])) 
# 시작시간은 같은데 끝나는 시간이 다를 수 있으니 모두 정렬해야 함(반대)

cnt = 0
meet = 0
for i in arr:
    if meet <= i[0]: 
# 앞 미팅의 끝나는 시간이 뒷 미팅의 시작 시간보다 이르면
        cnt += 1
        meet = i[1]
# 앞 미팅을 뒷 미팅으로 간주(앞 미팅의 끝나는 시간 저장, 그 앞 미팅의 끝나는 시간과 비교하기 위함)

print(cnt)