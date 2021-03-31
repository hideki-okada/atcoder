N = int(input())
for i in range(10):
    if (i + 1) * 1000 >= N:
        print((i + 1) * 1000 - N)
        break

