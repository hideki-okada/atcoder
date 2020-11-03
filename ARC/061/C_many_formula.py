# 文字列Sの文字数をNとするとN-1箇所に+を入れることができるので、2 ** N-1通りの計算式があり得る。
# それを全探索で潰す
from copy import deepcopy

S = input()
N = len(S)
ans = 0
for i in range(2 ** (N - 1)):
    plus_count = 0
    tmp_s = deepcopy(S)
    for j in range(N - 1):
        if i >> j & 1:
            tmp_s = tmp_s[:1 + j + plus_count] + '+' + tmp_s[1 + j + plus_count:]
            plus_count += 1
    ans += eval(tmp_s)
print(ans)