import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

print(min(x), max(x))