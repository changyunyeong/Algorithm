arr = [0] * 26
cnt = 0

for i in input(): # i는 문자
    arr[ord(i) - 97] += 1 # 알파벳 저장
for j in input():
    arr[ord(j) - 97] -= 1 # 겹치면 위에 배열에서 제거하기 때문에 0으로 됨

print(sum(map(abs, arr)))
# 0이 아니면 겹치는 글자가 아니므로 절댓값으로 바꾼 후 계산