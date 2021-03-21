N = int(input())
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    if i == 0:
        prev_a = a
    else:
        if a < prev_a:
            ans += (prev_a - a)
        else:
            prev_a = a
print(ans)
