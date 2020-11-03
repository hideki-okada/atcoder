import numpy as np

c = [list(map(int, input().split())) for i in range(3)]
c = np.array(c)
flag = False
for a1 in range(min(c[0]) + 1):
    b1 = c[0, 0] - a1
    b2 = c[0, 1] - a1
    b3 = c[0, 2] - a1
    if c[1, 0] - b1 == c[1, 1] - b2 == c[1, 2] - b3 and c[2, 0] - b1 == c[2, 1] - b2 == c[2, 2] - b3:
        print('Yes')
        flag = True
        break
if not flag:
    print('No')
