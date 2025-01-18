# linked list
from sys import stdin

# self: 객체 자기 자신을 참조하는 매개변수 => 클래스 내에 정의한 멤버에 접근 가능
# 쓰임새 봐선 this 인 듯
 
## 경우 1: 링크드 리스트 ##

class ListNode:
    def __init__(self, val, prev, next): 
        self.val = val
        self.prev = prev
        self.next = next

head = ListNode("dummy", None, None)
cur = head

init = input() # 초기 문자열
for i in range (len(init)):
    newNode = ListNode(init[i], None, None) # 새로운 노드 생성
    cur.next = newNode
    newNode.prev = cur # 맨 첨엔 head인 줄 알았는데 커서를 옮겨줘야 하니 커서가 더 적당할 듯
    cur = newNode

for _ in range(int(input())): # 명령어 처리
    command = stdin.readline().rstrip() # rstrip: 특정 문자 제거 (오른쪽)
    if command == "L":
        if cur.val != "dummy": # head면 무시됨
            cur = cur.prev
    elif command == "D":
        if cur.next: # 맨 뒤는 무시됨
            cur = cur.next
    elif command == "B": # head면 무시됨
        if cur.val != "dummy":
            cur = cur.prev
            if cur.next.next:
                cur.next = cur.next.next
                cur.next.prev = cur
            else:
                cur.next = None
    else:
        newNode = ListNode(command[-1], None, None)
        if cur.next:
            newNode.next = cur.next
            cur.next.prev = newNode
        cur.next = newNode
        newNode.prev = cur
        cur = newNode

printNode = head.next
while printNode:
    print(printNode.val, end='')
    printNode = printNode.next
    




## 경우 2: 스택 ##

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right [::-1]
print(''.join(answer))