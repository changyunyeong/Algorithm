import sys
from collections import Counter
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

x = Counter(arr).most_common()

for a,b in x:
    for _ in range(b):
        print(a, end = ' ')