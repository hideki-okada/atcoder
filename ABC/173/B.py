N = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(N):
    s = input()
    if s == 'AC':
        ac += 1
    elif s == 'WA':
        wa += 1
    elif s == 'TLE':
        tle += 1
    else:
        re += 1
print(f'AC x {ac}')
print(f'WA x {wa}')
print(f'TLE x {tle}')
print(f'RE x {re}')
