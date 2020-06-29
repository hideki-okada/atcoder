from collections import deque

N, M = list(map(int, input().split()))
relation_list = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = list(map(int, input().split()))
    relation_list[a].append(b)
    relation_list[b].append(a)

room_q = deque()
room_q.append(1)
michihsirube_room = [-1 for _ in range(N + 1)]
while room_q:
    node = room_q.popleft()
    for near_room_id in relation_list[node]:
        if michihsirube_room[near_room_id] == -1:
            michihsirube_room[near_room_id] = node
            room_q.append(near_room_id)
print('Yes')
for i in range(2, N + 1):
    print(michihsirube_room[i])
