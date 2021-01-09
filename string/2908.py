
a, b = input().split()
A = a[::-1]
B = b[::-1]

if A > B:
    print(A)
elif A < B:
    print(B)