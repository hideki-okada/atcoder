N = int(input())
colors = input()
red_index = []
white_index = []
for i, c in enumerate(colors):
    if c == 'R':
        red_index.append(i)
count = 0
for red_i in red_index:
    if red_i < len(red_index):
        count += 1
print(len(red_index) - count)
