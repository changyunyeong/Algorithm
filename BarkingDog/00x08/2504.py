string = input()
stack = []
cnt = 0
temp = 1

for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        temp *= 2
    elif string[i] == '[':
        stack.append(string[i])
        temp *= 3
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            cnt = 0
            break
        if string[i-1] == '(':
            cnt += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            cnt = 0
            break
        if string[i-1] == '[':
            cnt += temp
        temp //= 3
        stack.pop()
              
print(0 if stack else cnt)