N, K = map(int, input().split())
d = []
ans = []
for i in range(K):
    d = int(input())
    ans.extend(list(map(int, input().split())))
ans = set(ans)
print(N - len(ans))