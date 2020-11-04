# 区間スケジューリング
# 基本的に端っこよりは中にいるロボットの方が重複しやすいので、中にいるロボットを除くことを繰り返していけばよい

N = int(input())
robot_range = []
for i in range(N):
    x, arm = map(int, input().split())
    left, right = x - arm, x + arm
    robot_range.append([left, right])
robot_range = sorted(robot_range, key=lambda x: x[1])
remove_robot_num = []
for i, (left, right) in enumerate(robot_range):
    if i == 0:
        prev_right = right
    else:
        if prev_right > left:
            remove_robot_num.append(i)
        else:
            prev_right = right
print(N - len(remove_robot_num))
