import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))

arr.sort(key = lambda x:x[0]) # age, name에서 0번째 요소인 age만 비교

for i in arr:
    print(i[0], i[1]) # 첫 번째 요소랑 두 번째 요소 출력 (나이, 이름)