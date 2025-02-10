import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    left = []
    right = []
    command = input().strip()
    
    for i in command:

        if i == '<':
            if left: # and left는 left 안에 요소가 있냐이고 if left면 현재 left에 있는 것인지 판단단
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
        
    left.extend(reversed(right))
    print(''.join(left))
    
# if left:는 단독으로 실행될 때 left가 비어 있지 않으면 항상 True이므로 리스트 조작이 정상적으로 이루어짐
# if i == '<' and left:를 사용하면 "<" 문자가 들어오지 않으면 left가 비어 있는지를 검사하지 않기 때문에 예상치 못한 동작이 발생할 수 있음