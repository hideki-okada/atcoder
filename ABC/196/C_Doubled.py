N = int(input())
# Nの桁数を出す
keta = len(str(N))
ruisekiwa = [9, 90, 900, 9000, 90000, 9000000]
# 桁数に応じて計算
if keta == 1:
    print(0)
elif keta % 2 == 1:
    ans = sum(ruisekiwa[:(keta - 1) // 2])
    print(ans)
else:
    zenhan = N // (10 ** (keta / 2))
    kouhan = N - zenhan * (10 ** (keta / 2))
    if zenhan <= kouhan:
        ans = sum(ruisekiwa[:(keta // 2 - 1)]) + N // 10 ** (keta // 2) - 10 ** (keta // 2 - 1) + 1
    else:
        ans = sum(ruisekiwa[:(keta // 2 - 1)]) + N // 10 ** (keta // 2) - 10 ** (keta // 2 - 1)
    print(ans)
