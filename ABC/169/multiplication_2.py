N = int(input())
a = list(map(int, input().split()))
if 0 in a:
    print(0)
else:
    ans = 1
    for i in range(N):
        ans *= a[i]
        if ans > 10 ** 18:
            break
    if ans > 10 ** 18:
        print(-1)
    else:
        print(ans)
