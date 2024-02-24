import sys
input = sys.stdin.read

n, *s = input().split() # *s: 정해지지 않은 개수의 입력값 들어옴

for i in range(int(n)):
    # s1 = reversed(s)
    s[i] = s[i][::-1]

s = list(map(int, s))
print(*sorted(s), sep = "\n")
# sep = separation (구분자)

# print('S','E','P', sep='@')
# 출력 >>>>> S@E@P