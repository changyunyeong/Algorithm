import math

n, k = map(int, input().split()) # 학생 수 # 최대 인원 수
arr = [[0]*7 for _ in range(3)] # 성별 / 학년 2차원 배열
ans = 0

for _ in range(n):
    s, y = map(int, input().split())
    arr[s][y] += 1

# for i in range(3):
#     for j in range(7):
#         if(arr[i][j] % k == 0):
#             ans += [j][i] / k
#         else:
#             ans += [j][i] // k + 1 # //: 정수값만

for i in arr:
    for j in i:
        ans += math.ceil(j / k)
print (ans)

# ceil: x 올림값 반환