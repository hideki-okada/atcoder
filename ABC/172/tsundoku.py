import sys

sys.setrecursionlimit(200000000)

N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_num = 0

def dfs(curr_a, curr_b, choice, time_required, count):
    global max_num
    if choice == 0:
        if curr_a >= N - 1:
            if max_num < count:
                max_num = count
            return
        else:
            curr_a += 1
            time_required += a[curr_a]
    else:
        if curr_b >= M - 1:
            if max_num < count:
                max_num = count
            return
        else:
            curr_b += 1
            time_required += b[curr_b]
    if time_required > K:
        return
    count += 1
    if max_num < count:
        max_num = count
    dfs(curr_a, curr_b, 0, time_required, count)
    dfs(curr_a, curr_b, 1, time_required, count)


if sum(a) + sum(b) <= K:
    print(N + M)
else:
    curr_a = -1
    curr_b = -1
    time_required = 0
    count = 0
    dfs(curr_a, curr_b, 0, time_required, count)
    curr_a = -1
    curr_b = -1
    time_required = 0
    count = 0
    dfs(curr_a, curr_b, 1, time_required, count)
    print(max_num)
