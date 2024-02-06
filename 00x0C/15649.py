n, m = map(int, input().split())
arr = []

def fun():
    if len(arr) == m: # m개를 모두 선택 시 (정답이면)
        print(" ".join(map(str, arr))) # 배열 출력
        return
     
    for i in range(1, n+1): # 1부터 n
        if i not in arr: # i가 사용되지 않았으면 (중복이 아니면)
            arr.append(i) # 숫자 i 저장
            fun() # 재귀
            arr.pop()

#   -> 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.

#       s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]

#                   출력   pop(2)  출력   pop(3)  출력

fun()

# 백트래킹: 주어진 기준대로 "원소의 순서"를 선택하는 데에 적합