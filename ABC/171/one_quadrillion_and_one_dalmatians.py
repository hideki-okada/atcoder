N = int(input())


def num2alpha(num):
    if num <= 26:
        return chr(64 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(90)
    else:
        return num2alpha(num // 26) + chr(64 + num % 26)


def main():
    print(num2alpha(N).lower())


main()

'''
tmp = 26
ret = 0
keta = 1
while True:
    if N - tmp > 0:
        ret = N - tmp
        tmp *= 26
        keta += 1
    else:
        break

for i in range(keta):
    ans += ''
'''
