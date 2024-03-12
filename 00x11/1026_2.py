import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a는 정렬 가능
ans = 0

for i in range(n):
    bMax = max(b)
    ans += a[i]*bMax
    b.remove(bMax)

print(ans)
# 이 풀이가 좀 더 좋아보임
# 맨 처음엔 인덱스를 하나하나 변화시킬 생각이었음