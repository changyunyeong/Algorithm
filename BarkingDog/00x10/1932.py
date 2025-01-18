import sys
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == len(d[i])-1:
            d[i][j] += d[i-1][j-1]
        else: 
            d[i][j] += max(d[i-1][j-1], d[i-1][j])
    
print(max(d[n-1]))