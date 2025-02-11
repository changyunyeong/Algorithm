import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip() 
    n = int(input().strip())
    arr = input().strip()
    
    dq = deque(arr[1:-1].split(',')) if arr[1:-1] else deque()  # 빈 배열 처리
    reverse_flag = False
    
    try:
        for i in p:
            if i == 'R':
                reverse_flag = not reverse_flag
            elif i == 'D':
                if dq:
                    if reverse_flag:
                        dq.pop()
                    else:
                        dq.popleft()
                else:
                    raise ValueError
        
        if reverse_flag:
            dq.reverse() # reverse는 O(n)이므로 한 번만 사용
        
        print('[' + ",".join(dq)+']')
        
    except:
        print('error')