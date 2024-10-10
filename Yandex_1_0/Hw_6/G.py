def get_max_width(n, m, t):
    left = 0
    right = n + m

    while left < right:
        index = (left + right + 1) // 2
        if m - 2 * index < 0:
            right = index - 1
            continue
        if 2 * (n * index) + 2 * ((m - 2 * index) * index) <= t:
            left = index
        else:
            right = index - 1

    return left


n = int(input())
m = int(input())
t = int(input())
print(get_max_width(n, m, t))
