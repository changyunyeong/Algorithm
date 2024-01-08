import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    p = input().rstrip()
    n = int(input())
    dq = deque(input().rstrip()[1:-1].split(",")) # 대괄호를 제외하고 내부의 숫자만 선택
    
    for j in p:
        if j == "R":
            dq.reverse()
        elif j == "D":
            if len(dq) != 0:
                dq.popleft()
            else:
                print("error")
    
    print("[" + ",".join(dq) + "]")