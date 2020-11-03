N = int(input())
t = [int(input()) for _ in range(N)]

min_time = 200

for i in range(2 ** N):
    nikuyaki_0 = 0
    nikuyaki_1 = 0
    for j in range(N):
        if (i >> j) & 1:
            nikuyaki_1 += t[j]
        else:
            nikuyaki_0 += t[j]
    tm = max(nikuyaki_0, nikuyaki_1)
    if tm < min_time:
        min_time = tm
print(min_time)
