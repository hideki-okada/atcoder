A, B, C, D = map(int, input().split())
while True:
    C -= B
    if C <= 0:
        win_takahashi = 'Yes'
        break
    A -= D
    if A <= 0:
        win_takahashi = 'No'
        break
print(win_takahashi)
