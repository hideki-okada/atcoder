# 辞書式問題の中で最難関では、むずすぎた


from collections import Counter
from copy import deepcopy


def cal_huicchi(s: str, t: str):
    count_s = Counter(s)
    count_t = Counter(t)
    alphabet_list = [chr(ord("a") + i) for i in range(26)]
    icchi = 0
    for c in alphabet_list:
        icchi += min(count_s[c], count_t[c])
    return len(s) - icchi


N, K = map(int, input().split())
S = input()
sorted_nokori_s = sorted(S)
T = ''
cur_huicchi = 0
for i in range(N):
    for j, c in enumerate(sorted_nokori_s):
        nokori = sorted_nokori_s[:j] + sorted_nokori_s[j + 1:]
        tmp_huicchi = deepcopy(cur_huicchi)
        if S[i] != c:
            tmp_huicchi += 1
        if tmp_huicchi + cal_huicchi(S[i + 1:], ''.join(nokori)) <= K:
            cur_huicchi = tmp_huicchi
            T = T + c
            sorted_nokori_s.pop(j)
            break
print(T)