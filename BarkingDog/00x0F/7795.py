import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    na, nb = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort() # 정렬함으로서 비교하는 데 걸리는 시간 단축
    # 정렬 안 하면 시간초과 남
    
    cnt = 0
    start = 0
    
    for i in range(na):
        while True:
            if start == nb or a[i] <= b[start]:
                cnt += start
                break
            else:
                start += 1
    
    print(cnt)