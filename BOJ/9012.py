import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = input()
    temp = []
    
    for i in arr:
        if i == '(':
            temp.append(i)
        if i == ')':
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(i)
    
    print("YES" if not temp else "NO")