n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]: # if aaabc면 j=0에서 pass이므로 elif 문 실행하지 않음 
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)

for _ in range(n):
    word = input()
    seen = set()
    prev = ""
    
    for char in word:
        if char != prev: # 연속된 문자가 아닐 때
            if char in seen: # 이전에 등장한 단어라면 제거 
                cnt -= 1
                break
            seen.add(char)
        prev = char
print(cnt)