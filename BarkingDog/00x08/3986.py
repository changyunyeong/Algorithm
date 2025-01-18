n = int(input())
cnt = 0

for i in range(n):
    arr = input()
    stack = []
    
    for j in arr:
        if j == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(j)
        elif j == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(j)
    
    if len(stack) == 0:
        cnt += 1

print(cnt)