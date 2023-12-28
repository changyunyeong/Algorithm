n = int(input())

for _ in range(n):
    a,b = map(str, input().split())
    a = list(a)
    a.sort()
    b = list(b)
    b.sort()
    
    if (len(a) != len(b)): # 단어의 길이가 다를 경우
        print("Impossible")
        continue
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break
        else:
            flag = True
    if flag:
        print("Possible")
    else:
        print("Impossible")