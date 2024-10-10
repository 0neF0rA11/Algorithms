def get_min_time(n, x, y):
    x, y = sorted([x, y])

    left, right = 0, n * y
    while left < right:
        index = (left + right) // 2
        if index // x + index // y >= n - 1:
            right = index
        else:
            left = index + 1
    return left + x


n, x, y = map(int, input().split())
print(get_min_time(n, x, y))
