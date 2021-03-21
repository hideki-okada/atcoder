A, B, W = map(int, input().split())
W = W * 1000
if W // B == W // A:
    if W % B == 0 and W % A == 0:
        print(W // B, W // A)
    else:
        print("UNSATISFIABLE")
else:
    min_orange = W // B + 1 if W % B > 0 else W // B
    max_orange = W // A
    print(min_orange, max_orange)
