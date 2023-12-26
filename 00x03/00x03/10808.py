s = input()
list = [0]*26 
# 알파벳 26개 -> 배열 인덱스 26으로 초기화

# for i in s:
#     list[ord(i)-97] += 1
#     # 'a' = 97 -> list와 index 통일

# for i in list:
#     print(i, end=' ')

for str in s:
    list[ord(str)-97] = s.count(str)
print(*list)

# string.count(찾을 문자열, 시작, 끝) 숫자로 리턴