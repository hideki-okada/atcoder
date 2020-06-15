A, R, N = map(int, input().split())
ans = A
large_flag = False
if R == 1:
    print(ans)
else:
    for i in range(N - 1):
        ans *= R
        if ans > 10 ** 9:
            large_flag = 1
            break

    if large_flag:
        print('large')
    else:
        print(ans)
