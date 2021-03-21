import numpy as np
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = np.array(AB)
A = AB[:, 0]
B = AB[:, 1]
order_A = np.argsort(A)
order_B = np.argsort(B)
if order_A[0] != order_B[0]:
    print(max(A[order_A[0]], B[order_B[0]]))
else:
    print(min(A[order_A[0]]+B[order_B[0]], max(A[order_A[0]], B[order_B[1]]), max(A[order_A[1]], B[order_B[0]])))