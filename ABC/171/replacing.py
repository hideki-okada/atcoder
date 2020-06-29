from collections import Counter
N = int(input())
a = list(map(int, input().split()))
Q = int(input())
bc = [list(map(int, input().split())) for _ in range(Q)]
tmp_counter = Counter(a)
tmp_sum = sum(a)
for b, c in bc:
    if b in tmp_counter.keys():
        tmp_sum += (c - b) * tmp_counter[b]
        tmp_counter[c] += tmp_counter[b]
        tmp_counter[b] = 0
    print(tmp_sum)
