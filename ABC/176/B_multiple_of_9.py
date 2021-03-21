N = input()
total = 0
for n in N:
    total += int(n)
if total % 9 == 0:
    print('Yes')
else:
    print('No')
