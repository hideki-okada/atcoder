from collections import deque

X, N = map(int, input().split())
p = list(map(int, input().split()))
ans = X
queue = deque()
queue.append(X)
done_list = []
ans = []
while queue:
    var = queue.popleft()
    if var in p:
        done_list.append(var)
        if var - 1 not in done_list:
            queue.append(var-1)
        if var + 1 not in done_list:
            queue.append(var+1)
        continue
    else:
        ans = var
        break
print(ans)