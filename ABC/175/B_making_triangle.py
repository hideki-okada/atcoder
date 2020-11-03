import itertools

N = int(input())
L = list(map(int, input().split()))
index_list = [i for i in range(N)]
count = 0
for v in itertools.combinations(index_list, 3):
    if L[v[0]] == L[v[1]] or L[v[1]] == L[v[2]] or L[v[2]] == L[v[0]]:
        continue
    elif L[v[0]] + L[v[1]] <= L[v[2]] or L[v[1]] + L[v[2]] <= L[v[0]] or L[v[2]] + L[v[0]] <= L[v[1]]:
        continue
    else:
        count += 1
print(count)

