import sys
input = sys.stdin.readline

arr = []
string = input().split("-") # - 기준으로 split

for i  in string:
    sum = 0
    temp = i.split("+") # 덧셈 하기 위해 + 기준으로 split
    for j in temp:
        sum += int(j) #  3 + 4에서 3,4 분리 -> int 로 형변환 -> 덧셈
    arr.append(sum)
    
num = arr[0] # 제일 처음은 숫자로 시작하니까 0번째 값에서 나머지를 뺀다
for i in range(len(arr)):
    num -= arr[i]

print(num)