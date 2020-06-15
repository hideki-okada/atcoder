import sys


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    N_mat = []
    M_mat = [-1 for _ in range(M)]
    for i, taste in enumerate(a):
        if len(N_mat) == 0 or taste <= min(N_mat):
            if len(N_mat) == N:
                continue
            else:
                N_mat.append(taste)
                M_mat[i] = len(N_mat)
        else:
            for j, st in enumerate(N_mat):
                if st < taste:
                    N_mat[j] = taste
                    M_mat[i] = j + 1
                    break
    for m in M_mat:
        print(m)


if __name__ == '__main__':
    main()
