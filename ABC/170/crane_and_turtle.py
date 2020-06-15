X, Y = list(map(int, input().split()))
if Y%2==0 and (X * 2 <= Y <= X * 4):
    print('Yes')
else:
    print('No')
