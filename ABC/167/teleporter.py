N, K = map(int, input().split())
a = list(map(int, input().split()))

rireki = [0] * (2 * 10 ** 5 + 1)
flag = [[] for _ in range(2 * 10 ** 5 + 1)]
rireki[0] = 1
flag[1].append(0)
count = 0
roop_start = 0
roop_count = 0
while True:
    count += 1
    rireki[count] = a[rireki[count - 1] - 1]
    flag[rireki[count]].append(count)
    if len(flag[rireki[count]]) == 2:
        roop_start = flag[rireki[count]][0]
        roop_count = flag[rireki[count]][1] - flag[rireki[count]][0]
        break
    if count == K:
        break
if roop_count != 0:
    print(rireki[(K - roop_start) % roop_count + roop_start])
else:
    print(rireki[K])
