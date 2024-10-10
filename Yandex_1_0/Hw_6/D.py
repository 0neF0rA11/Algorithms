def calculate_protection_size(n, a, b, w, h):
    left, right = 0, min(w, h)
    while left < right:
        size = (left + right + 1) // 2
        if (w // (a + 2 * size)) * (h // (b + 2 * size)) >= n or \
           (w // (b + 2 * size)) * (h // (a + 2 * size)) >= n:
            left = size
        else:
            right = size -1

    return left


n, a, b, w, h = map(int, input().split())
print(calculate_protection_size(n, a, b, w, h))
