import numpy as np

N = int(input())
A = list(map(int, input().split()))
cum_sum = np.cumsum(A)
sum_squared = (N - 1) * sum([x ** 2 for x in A])
sum_diff = 0
for i in range(N - 1, 0, -1):
    sum_diff += A[i] * (cum_sum[i - 1])
print(sum_squared - 2 * sum_diff)
