import numpy as np
x = list(map(int, input().split()))
x = np.array(x)
print(np.where(x==0)[0][0] + 1)