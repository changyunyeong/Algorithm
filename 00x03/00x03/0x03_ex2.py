list = [0]*100
def func2(arr, n):
    for i in n:
        if list[100 - arr[i]]:
            return 1
        # 53이 나왔을 때 이전에 47이 등장했는지 확인
        else:
            return 0