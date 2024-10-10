def can_form_teams(heights, R, C, max_diff):
    n = len(heights)
    team_count = 0
    i = 0
    while i <= n - C:

        if heights[i + C - 1] - heights[i] <= max_diff:
            team_count += 1
            i += C
        else:
            i += 1

        if team_count >= R:
            return True

    return team_count >= R


def minimize_max_discomfort(heights, R, C):
    heights.sort()
    left, right = 0, heights[-1] - heights[0]

    while left < right:
        mid = (left + right) // 2
        if can_form_teams(heights, R, C, mid):
            right = mid
        else:
            left = mid + 1

    return left


N, R, C = map(int, input().split())
heights = []
for i in range(N):
    heights.append(int(input()))

print(minimize_max_discomfort(heights, R, C))