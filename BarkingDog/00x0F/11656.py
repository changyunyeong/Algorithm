s = str(input())
arr = []
for i in range(len(s)):
    arr.append(s[i:]) # 0번째~ 1번째~

arr.sort()
for i in range(len(s)):
    print(arr[i])