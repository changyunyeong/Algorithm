arr = []
for i in range(9):
    arr.append(int(input()))
max = 0
for i in range(9):
    if arr[i] > max:
        max = arr[i]
        temp = i
print(arr[temp])
print(temp+1)

nums = [int(input()) for _ in range(9)] # 한 번에 입력받기
print(max(nums))
print(nums.index(max(nums))+1)