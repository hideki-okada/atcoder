from collections import Counter
from copy import deepcopy

N = int(input())
bin_X = input()
dec_X = int(bin_X, 2)
X = list(bin_X)
total = Counter(X)['1']
amari_table = [None] * (total + 2)
amari_table[0] = 1
for i in range(N):
    tmp_total = deepcopy(total)
    if X[i] == '1':
        tmp_total -= 1
        tmp_dec_X = dec_X - 2 ** (N - i - 1)
    else:
        tmp_total += 1
        tmp_dec_X = dec_X + 2 ** (N - i - 1)
    amari = tmp_dec_X % tmp_total
    if amari_table[amari] is not None:
        print(amari_table[amari])
    else:
        count = 1
        orig_amari = deepcopy(amari)
        while True:
            tmp_total = Counter(bin(amari))['1']
            amari %= tmp_total
            count += 1
            if amari == 0:
                break
        amari_table[orig_amari] = count
        print(count)
