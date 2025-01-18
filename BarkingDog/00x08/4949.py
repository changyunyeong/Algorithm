while True:
    stack = []
    string = input()
    
    if string == '.':
        break
    
    for i in string:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")