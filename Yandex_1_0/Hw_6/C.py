def calculate_size_board(w, h, n):
    left, right = 0, 10**15
    while left < right:
        index = (left + right) // 2
        if ((index // w) * (index // h)) >= n:
            right = index
        else:
            left = index + 1
    return left


w, h, n = map(int, input().split())
print(calculate_size_board(w, h, n))
