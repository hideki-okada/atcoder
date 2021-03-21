N = int(input())
current_i = N
count = -1
while current_i > 0:
    current_i = current_i // 10
    count += 1
if count // 3 == 5:
    print((10 ** 6 - 10 ** 3) + (10 ** 9 - 10 ** 6) * 2 + (10 ** 12 - 10 ** 9) * 3 + (10 ** 15 - 10 ** 12) * 4 + 5)
elif count // 3 == 4:
    ans = (10 ** 6 - 10 ** 3) + (10 ** 9 - 10 ** 6) * 2 + (10 ** 12 - 10 ** 9) * 3 + (N - 10 ** 12 + 1) * 4
    print(ans)
elif count // 3 == 3:
    ans = (10 ** 6 - 10 ** 3) + (10 ** 9 - 10 ** 6) * 2 + (N - 10 ** 9 + 1) * 3
    print(ans)
elif count // 3 == 2:
    ans = (10 ** 6 - 10 ** 3) + (N - 10 ** 6 + 1) * 2
    print(ans)
elif count // 3 == 1:
    ans = (N - 10 ** 3 + 1)
    print(ans)
else:
    print(0)
