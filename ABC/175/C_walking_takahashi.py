X, K, D = map(int, input().split())
N = abs(X) / D
if K < N:
    print(abs(abs(X) - D * K))
elif (K - round(N)) % 2 == 0:
    print(abs(abs(X) - D * round(N)))
elif round(N) - N >= 0:
    print(abs(abs(X) - (round(N) - 1) * D))
else:
    print(abs(abs(X) - (round(N) + 1) * D))

