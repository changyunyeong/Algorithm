n = int(input()) # 수열의 크기
arr1 = list(map(int, input().split())) # 수열
x = int(input())
arr2 = [0] * 2000000
cnt = 0

for i in range(n):
    if arr2[x-arr1[i]]:
        cnt += 1
    arr2[arr1[i]] = 1
    
print(cnt)

# https://daydreamx.tistory.com/entry/baekjoon3273
# 댜른 사람 풀이 참고용