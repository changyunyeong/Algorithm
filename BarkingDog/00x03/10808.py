import sys
input = sys.stdin.readline

s = input().strip()
arr = [0]*26 # a-z 26개

for i in s:
    arr[ord(i)-97] += 1

print(*arr)

# ord('a') = 97

for str in s:
    list[ord(str)-97] = s.count(str) # count는 O(N^2)
print(*list) # 리스트 요소 공백 기준으로 나열