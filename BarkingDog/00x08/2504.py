string = input()
stack = []
pre = 0
cnt = 0

for i in string:
    if i == '[':
        stack.append(i)
    elif i == ']' and pre == ']':
        cnt = cnt * 3
        stack.pop()
    elif i == ']' and pre != ']':
        cnt = cnt + 3
        stack.pop()
    
    elif i == '(':
        stack.append(i)
    elif i == ')' and pre == ')':
        cnt = cnt * 2
        stack.pop()
    elif i == ')' and pre != ')':
        cnt = cnt + 2
        stack.pop()
    
    pre = i
    
if len(stack) != 0:
    print(0)
else:
    print(cnt)