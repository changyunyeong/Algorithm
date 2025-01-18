import sys
input = sys.stdin.readline

s = input()
cnt = 0

for i in range(len(s)-1):
    if s[i]!=s[i-1]:
        cnt+=1

print(cnt//2) 
# 한 번만 뒤집으면 되는데 숫자가 바뀔 때마다 cnt가 올라가니 //2