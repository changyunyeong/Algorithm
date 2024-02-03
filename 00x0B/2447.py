# 재귀는 n부터 생각할 것!
# function define -> base condition -> recursion
n = int(input())

def fun(n):
    star = []
    
    if n == 1:
        return ['*']
    
    ans = fun(n//3)
    
    for i in ans:
        star.append(i*3)
    for i in ans:
        star.append(i + " "*(n//3) + i) # 빈칸 9,3,1
    for i in ans:
        star.append(i*3)
    
    return star

print('\n'.join(fun(n)))

# 배열에 별 하나씩 append 한다는 생각을 못 했음 (단순 반복문으로만 접근)