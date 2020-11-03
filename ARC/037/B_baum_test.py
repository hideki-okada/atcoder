import sys

sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
relation = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    relation[u].append(v)
    relation[v].append(u)
seen = [0] * (N + 1)
seen[0] = 1


def dfs(cur_node: int, prev_node: int):
    global has_loop
    seen[cur_node] = 1
    print(cur_node, relation[cur_node])
    if not relation[cur_node]:
        return True
    for next_node in relation[cur_node]:
        if next_node == prev_node:
            continue
        elif seen[next_node] == 1:
            has_loop = 1
        else:
            dfs(next_node, cur_node)


if __name__ == '__main__':
    count = 0
    while True:
        has_loop = 0
        if sum(seen) == len(seen):
            break
        ans = dfs(seen.index(0), 0)
        if not has_loop:
            count += 1

    print(count)
