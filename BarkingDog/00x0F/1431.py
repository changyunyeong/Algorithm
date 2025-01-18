import sys
input = sys.stdin.readline

n = int(input())

ans = []
for _ in range(n):
    arr = input().rstrip() # string 오른쪽에서 제거
    
    sum = 0
    
    for i in arr:
        if i.isdigit(): 
            sum += int(i) # 정수로 반환
    ans.append((arr, sum)) # 각 자리수의 합 구하기 위함

ans.sort(key = lambda x:(len(x[0]), x[1], x[0]))
# 문자열의 길이(len(arr)), 숫자의 합(sum), 문자열 사전 순

for i in ans:
    print(i[0])