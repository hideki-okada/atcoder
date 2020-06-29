from sys import stdin

U = 10 ** 6 + 10


def main():
    readline = stdin.readline
    _ = int(readline())
    a = list(map(int, readline().split()))[1:]
    ret = 0
    exist_counts = [0] * U
    for x in a:
        if exist_counts[x]:
            exist_counts[x] = 2
            continue
        idx = x
        while idx < U:
            exist_counts[idx] += 1
            idx += x
    for x in a:
        ret += exist_counts[x] == 1
    print(ret)


main()
