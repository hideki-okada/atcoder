A, B, N = map(int, input().split())
print((A * min(B - 1, N) // B) - A * (min(B - 1, N) // B))
