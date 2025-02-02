import sys
input = sys.stdin.readline

n = input()
arr = []
for i in n:
    arr.append(i)
    
arr.sort(reverse=True) # 내림차순

for i in arr:
    print(i, end='') # \n 제거 