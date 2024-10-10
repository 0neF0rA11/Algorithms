def near_colors(n, t_colors, m, p_colors):
    t_colors = list(map(int, t_colors.split()))
    p_colors = list(map(int, p_colors.split()))

    left, right = 0, 0
    t_idx, p_idx = 0, 0
    min_delta = 10 ** 7

    while left < n and right < m:
        delta = abs(t_colors[left] - p_colors[right])
        if delta < min_delta:
            min_delta = delta
            t_idx = left
            p_idx = right

        if t_colors[left] == p_colors[right]:
            break
        elif t_colors[left] < p_colors[right]:
            left += 1
        else:
            right += 1

    return t_colors[t_idx], p_colors[p_idx]


n = int(input())
n_colors = input()
m = int(input())
m_colors = input()
print(*near_colors(n, n_colors, m, m_colors))