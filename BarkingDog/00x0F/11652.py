# n = int(input())
# temp = [0]*100000
# for i in range(n):
#     arr = int(input())
#     temp[arr-1] += 1

# max_value = max(temp) # temp 배열 중 가장 큰 값을 찾습니다.
# max_index = temp.index(max_value) # 가장 큰 값의 인덱스를 찾습니다.
# print(max_index + 1) # 인덱스를 출력합니다.

## 이렇게 하면 배열 크기 오류남 ##

import sys
input = sys.stdin.readline

n = int(input())
dic = {} # 딕셔너리는 중괄호

for i in range(n):
    card = int(input())
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1
    
result = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])