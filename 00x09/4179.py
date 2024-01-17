from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maze = []

for i in range(r):
    maze.append(list(map(str, input())))