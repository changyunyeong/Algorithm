cnt = 0
stack = []
string = input()
pre = '' # 이전에 등장한 문자 

for i in string:
    
    if i == '(':
        stack.append(i)
    elif i == ')' and pre == '(':
        stack.pop()
        cnt += len(stack)
    else:
        stack.pop()
        cnt += 1
    
    pre = i

print(cnt)