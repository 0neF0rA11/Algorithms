def get_min_and_max_time(a, b, n, m):
    min_1 = n + (n - 1) * a
    max_1 = (a + 1) * n + a

    min_2 = m + (m - 1) * b
    max_2 = (b + 1) * m + b
    max_time, min_time = min(max_1, max_2), max(min_1, min_2)

    if max_time < min_time:
        return -1

    return f"{min_time} {max_time}"


a, b = int(input()), int(input())
n, m = int(input()), int(input())
print(get_min_and_max_time(a, b, n, m))
