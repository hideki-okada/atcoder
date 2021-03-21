N, D = list(map(int, input().split()))
square_D = D ** 2
count = 0
for i in range(N):
    x, y = map(int, input().split())
    if x ** 2 + y ** 2 <= square_D:
        count += 1
print(count)
