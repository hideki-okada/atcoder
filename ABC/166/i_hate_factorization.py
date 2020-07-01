X = int(input())

for a in range(-118, 120):
    for b in range(-118, 120):
        if a**5 - b**5 == X:
            print(a, b)
            break
    else:
        continue
    break
