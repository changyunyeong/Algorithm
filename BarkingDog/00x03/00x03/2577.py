n1 = int(input())
n2 = int(input())
n3 = int(input())

num = list(str(n1 * n2 * n3))
# 문자열로 변환 후 배열 list로 묶음

for i in range(10):
    print(num.count(str(i)))
    # i가 0부터 9까지 증가 (숫자) -> 문자로 변환해 배열과 비교
    # count는 비교 함수임!!