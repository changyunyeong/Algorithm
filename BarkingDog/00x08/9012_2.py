for _ in range(int(input())):
    
    string = input()
    stack = []
    
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    
    print("YES" if not stack else "NO")