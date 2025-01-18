n = int(input())
arr = [0] * 10
# 각 숫자가 몇 번 나왔는지 저장하기 위한 배열

for i in str(n):     # 배열의 최댓값이 개수
    if i == "6" or i == "9":
        if arr[6] == arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
        # 6과 9는 구분하지 않기 때문에 두 배열의 값이 같으면 6, 다르면 9에 저장하도록 임의로 설정
    else:
        arr[int(i)] += 1
print(max(arr))