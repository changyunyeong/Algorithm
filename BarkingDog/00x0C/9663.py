import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n # 한 행에 두 개 이상 존재할 수 없기 때문에 퀸이 위치한 열 저장

def check(cur):
    for i in range(cur): # for 행 in 열
        # 같은 열 or 같은 대각성 (x+y, x-y) (그래서 열만 비교하는 거)
        if(arr[i] == arr[cur] or abs(arr[i]-arr[cur]) == abs(i-cur)):
            # 열 == 행
            return False
    
    return True

cnt = 0
def fun(cur): # cur번째 행에 Q 배치
    if cur == n:
        global cnt
        cnt += 1
    
    else:
        for i in range(n):
            arr[cur] = i
            if check(cur):
                fun(cur+1)

fun(0)
print(cnt)