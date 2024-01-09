stack = []
string = input()
sum = 0
pre = 0         # 이전에 등장한 문자열
    
for i in string:
    if i == '(':
        stack.append(i)
    elif i == ')' and  pre == '(': 
        stack.pop()
        sum += len(stack)
    else:
        stack.pop
        sum += 1
    
    pre = i

print(sum)