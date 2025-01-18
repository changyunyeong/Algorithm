import sys
input = sys.stdin.readline

n = int(input())
d = [0]*1000001 # 배열 초기화

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 1을 빼거나, 3으로 나누거나, 2로 나누거나
    # 3으로 나눠지거나 2로 나눠지거나를 계산할 때도 1을 빼는 것과 비교가 들어가기 때문에 미리 1을 빼야함
    # 1을 더하는 이유: 연산의 횟수가 1 증가하니까

print(d[n])