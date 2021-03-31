N = int(input())
count = [0] * (N + 1)
for x in range(1, 100):
    if 2 * ((x + 1) ** 2) + 4 > 2 * N:
        break
    for y in range(1, 100):
        if ((x + y) ** 2 + (y + 1) ** 2 + (1 + x) ** 2) > 2 * N:
            break
        for z in range(1, 100):
            # print(x, y, z)
            score = ((x + y) ** 2 + (y + z) ** 2 + (z + x) ** 2) // 2
            if score > N:
                break
            else:
                count[score] += 1
for i in range(1, N + 1):
    print(count[i])
