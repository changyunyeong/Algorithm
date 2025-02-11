import sys
input = sys.stdin.readline

n = int(input())
stack = []
operation = []
cnt = 1
check = True

for _ in range(n): # 입력은 오름차순이니 n만큼만 반복하면됨 
    num = int(input())
    
    while cnt <= num: # 접근 방식은 맞았는데 while을 생각 못했음  
        stack.append(cnt)
        operation.append('+')
        cnt += 1
    
    if stack[-1] == num: # 스택 제일 위에가 수열의 수랑 똑같으면
        stack.pop()
        operation.append('-')
    
    else:
        check = False
        break

if check == False:
    print("NO")
else:
    for i in operation:
        print(i)     