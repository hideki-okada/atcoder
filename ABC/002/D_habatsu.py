import itertools

N, M = map(int, input().split())
relation = [[0 for j in range(N + 1)] for i in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    relation[x][y] = 1
max_assemblyman = 0
for i in range(2 ** N):
    faction_member = []
    bad_flag = 0
    for j in range(N):
        if i >> j & 1:
            faction_member.append(j + 1)
    for v in itertools.combinations(faction_member, 2):
        if relation[v[0]][v[1]] != 1:
            bad_flag = 1
            break
    if not bad_flag and max_assemblyman < len(faction_member):
        max_assemblyman = len(faction_member)

print(max_assemblyman)
