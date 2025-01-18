n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0 and d[i] > d[i//2]+1:
        # 1로 뺐을 때 결과값이 2로 나눴을 때보다 크다면 2로 나누는 게 더 효율적이므로 2로 나눔
        d[i] = d[i//2] + 1
    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1

print(d[n])

while n!=1:
    print(n, end = ' ')
    if n%3==0 and d[n]==d[n//3]+1:
        # n을 3으로 나누는 연산이 최적의 연산이었다면
        n=n//3 # 그 결과값 출력
    elif n%2==0 and d[n]==d[n//2]+1:
        n=n//2
    else:
        n=n-1
print(1)