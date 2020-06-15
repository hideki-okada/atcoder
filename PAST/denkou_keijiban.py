import numpy as np


def distinguish_digits(arr: np.ndarray):
    if (arr[:, 0::2] == '#').all():
        if arr[2, 1] == '.':
            return 0
        else:
            return 8
    elif all(arr[:, 1] == '#'):
        return 1
    elif all(arr[:, 2] == '#') and (arr[0::2] == '#').all():
        if arr[1, 0] == '#':
            return 9
        else:
            return 3
    elif all(arr[:, 2] == '#'):
        if arr[0, 1] == '.':
            return 4
        else:
            return 7
    elif all(arr[:, 0] == '#'):
        return 6
    elif arr[1, 0] == '.':
        return 2
    else:
        return 5


N = int(input())
s = [list(input()) for _ in range(5)]
s = np.array(s)
ans_str = ''
for i in range(N):
    bubun = s[:, 4 * i + 1:4 * (i + 1)]
    ans = distinguish_digits(bubun)
    ans_str += str(ans)
print(ans_str)
