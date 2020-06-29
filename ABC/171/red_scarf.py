from collections import Counter

N = int(input())
a = list(map(int, input().split()))
a = [format(i, '019b') for i in a]
ans = [''] * N
for i in range(19):
    tmp = [int(t[i]) for t in a]
    if Counter(tmp)[0] % 2 == 0:
        for j in range(N):
            ans[j] += str(tmp[j])
    else:
        for j in range(N):
            if tmp[j]:
                ans[j] += str(0)
            else:
                ans[j] += str(1)
ans_b = [int('0b'+tp, 0) for tp in ans]
print(' '.join(map(str, ans_b)))
