cnt = 0

for _ in range(int(input())):
    string = input()
    stack = []
    
    for i in string:
        if i == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(i)
        elif i == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(i)
    
    if not stack:
        cnt += 1

print(cnt)