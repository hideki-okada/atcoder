N = int(input())
A = list(map(int, input().split()))
cur_A = max(A)
count = 0
while cur_A > 0:
    cur_A = cur_A // 2
    count += 1
count -= 1


def and_kukan(kukan1, kukan2):
    sorted_kukan = sorted([kukan1[0], kukan1[1], kukan2[0], kukan2[1]])
    if sorted_kukan[:2] == kukan1 or sorted_kukan[:2] == kukan2:
        return []
    else:
        return sorted_kukan[1:3]


kouho = []
ans = 0
for i in range(count, -1, -1):
    bit_count = []
    for j, a in enumerate(A):
        if a & (1 << i):
            bit_count.append(j)
    if len(bit_count) == 1:
        ans += 2 ** i
    elif len(bit_count) > 1:
        tmp_kouho = [bit_count[0], bit_count[-1]]
        if len(kouho) == 0:
            kouho = tmp_kouho
        else:
            new_kouho = and_kukan(kouho, tmp_kouho)
            if len(new_kouho) == 0:
                ans += 2 ** i
            else:
                kouho = new_kouho
    else:
        continue
print(ans)
