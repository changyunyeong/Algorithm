import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def fun(idx, sum):
    global cnt
    
    if idx >= n:
        return
    
    sum += arr[idx]

    if sum == s:
        cnt += 1
        
    fun(idx+1, sum) # arr[idx]를 선택했을 시 => 해당 인덱스가 sum에 추가
    fun(idx+1, sum - arr[idx]) # 선택 안 했을 때 => sum에서 해당 요소 값 빼기
    # 난 두 번째 걸 함수 내에서 조건으로 처리하려 했음
    
    return cnt

print(fun(0,0))         