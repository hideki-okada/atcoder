N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = A[0]
cur = 1
count = 1
while True:
    if count <= N - 3:
        ans += A[cur] * 2
        count += 2
        cur += 1
    elif count == N - 2:
        ans += A[cur]
        count += 1
    elif count == N - 1:
        break
print(ans)
