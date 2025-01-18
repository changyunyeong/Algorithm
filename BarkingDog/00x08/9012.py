t = int(input())

for i in range (t):
    stack = []
    string = input()
    
    for j in string:
        if j == '(':
            stack.append(j)
        if j == ')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(j)
                
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")