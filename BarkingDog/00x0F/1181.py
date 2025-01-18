n = int(input())
arr = [str(input()) for _ in range(n)]

arr = list(set(arr)) # 중복 제거
arr.sort() # 사전식 정렬
arr.sort(key = len) # 길이순 정렬

for i in arr:
    print(i)