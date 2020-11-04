# 区間ソート問題、区間の終端or始端でソートすると簡単になる

N, M = map(int, input().split())
request = [list(map(int, input().split())) for _ in range(M)]
request = sorted(request, key=lambda x: x[1])
remove_arch_num = []
for req in request:
    if len(remove_arch_num) == 0 or req[0] > remove_arch_num[-1]:
        remove_arch_num.append(req[1] - 1)
    else:
        continue
print(len(remove_arch_num))
