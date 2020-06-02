import numpy as np

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = np.array(arr)

if N % 2 == 1:
    a = np.sort(arr[:, 0])
    b = np.sort(arr[:, 1])
    print(b[N // 2] - a[N // 2] + 1)

else:
    a = np.sort(arr[:, 0])
    b = np.sort(arr[:, 1])
    print((b[N // 2] + b[N // 2 - 1]) - (a[N // 2 - 1] + a[N // 2]) + 1)
