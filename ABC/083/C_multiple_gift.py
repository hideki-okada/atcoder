# 母に数列Aをプレゼント
# AはX以上Y以下の整数からなる(1<=X<=Y<=10**18)
# 全ての1<=i<=|A|-1に対しA[i+1]はA[i]の倍数かつA[i+1]>A[i]
# 母にプレゼントできる数列の長さの最大値

X, Y = map(int, input().split())
ans = 1
while True:
    X *= 2
    if X <= Y:
        ans += 1
    else:
        break
    print(ans)
