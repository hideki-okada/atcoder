A, B, C, K = map(int, input().split())

if A + B + C >= K > A + B:
    print(A + -1 * (K - A - B))
elif A + B >= K > A:
    print(A)
else:
    print(K)
