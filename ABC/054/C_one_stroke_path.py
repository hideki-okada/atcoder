from copy import deepcopy


def dfs(relation, visited, start_node):
    global count
    seen = deepcopy(visited)
    seen.append(start_node)
    if len(seen) == N:
        count += 1
    for next_node in relation[start_node]:
        if next_node in seen:
            continue
        dfs(relation, seen, next_node)


if __name__ == '__main__':
    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]
    visited = []
    for i in range(M):
        x, y = map(int, input().split())
        relation[x].append(y)
        relation[y].append(x)
    count = 0
    dfs(relation, visited, 1)
    print(count)
