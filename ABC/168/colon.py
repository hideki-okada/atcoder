import math

A, B, H, M = list(map(int, input().split()))

theta = abs(6 * M - (60 * H + M) / 2)
if theta > 180:
    theta = 360 - theta
theta = abs(math.radians(theta))
ans = A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)
ans = math.sqrt(ans)
print(ans)
