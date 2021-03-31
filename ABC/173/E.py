mod = 10 ** 9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(key=lambda x: abs(x), reverse=True)
ans = 1
if N == K:
    for i in range(K):
        ans *= A[i]
        if abs(ans) > mod:
            ans %= mod
elif len([v for v in A if v < 0]) == N:
    for i in range(K):
        ans *= A[-(i + 1)]
        if abs(ans) > mod:
            ans %= mod
else:
    num_hu = len([v for v in A[:K] if v < 0])
    if num_hu % 2 == 0:
        for i in range(K):
            ans *= A[i]
            if abs(ans) > mod:
                ans %= mod
    else:
        if len([v for v in A[K:] if v >= 0]) == N - K:
            min_hu_idx = K - 1
            while True:
                if A[min_hu_idx] < 0:
                    break
                min_hu_idx -= 1
            max_sei_idx = K
            for i in range(K):
                if i == min_hu_idx:
                    ans *= A[max_sei_idx]
                else:
                    ans *= A[i]
                if abs(ans) > mod:
                    ans %= mod
        elif len([v for v in A[K:] if v <= 0]) == N - K:
            print('aaa')
            min_sei_idx = K - 1
            while True:
                if A[min_sei_idx] > 0:
                    break
                min_sei_idx -= 1
            max_hu_idx = K
            for i in range(K):
                if i == min_sei_idx:
                    ans *= A[max_hu_idx]
                else:
                    ans *= A[i]
                if abs(ans) > mod:
                    ans %= mod
        else:
            ans_1 = 1
            ans_2 = 1
            # ans_1
            min_hu_idx = K - 1
            while True:
                if A[min_hu_idx] < 0:
                    break
                min_hu_idx -= 1
            max_sei_idx = K
            while True:
                if A[max_sei_idx] > 0:
                    break
                max_sei_idx += 1
            for i in range(K):
                if i == min_hu_idx:
                    ans_1 *= A[max_sei_idx]
                else:
                    ans_1 *= A[i]
                if abs(ans_1) > mod:
                    ans_1 %= mod
            # ans_2
            min_sei_idx = K - 1
            while True:
                if A[min_sei_idx] > 0:
                    break
                min_sei_idx -= 1
            max_hu_idx = K
            while True:
                if A[max_hu_idx] < 0:
                    break
                max_hu_idx += 1
            for i in range(K):
                if i == min_sei_idx:
                    ans_2 *= A[max_hu_idx]
                else:
                    ans_2 *= A[i]
                if abs(ans_2) > mod:
                    ans_2 %= mod
            ans = max(ans_1, ans_2)
print(ans % mod)
