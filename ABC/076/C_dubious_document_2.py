s_dash = input()
t = input()
len_t = len(t)
ans_s = 'zzzzzzzzzz'
flag = 0
for i in range(len(s_dash) - len_t + 1):
    part_s_dash = s_dash[i:len_t + i]
    count = 0
    for j in range(len_t):
        if part_s_dash[j] == '?':
            count += 1
        elif part_s_dash[j] == t[j]:
            count += 1
        else:
            break
    if count == len_t:
        tmp_s = s_dash[:i] + t + s_dash[len_t + i:]
        tmp_s = tmp_s.replace('?', 'a')
        if tmp_s < ans_s:
            ans_s = tmp_s
        flag = 1
if flag:
    print(ans_s)
else:
    print('UNRESTORABLE')
