X = int(input())
money = 100
count = 0
while True:
    money = (money * 101) // 100
    count += 1
    if money >= X:
        break
print(count)
